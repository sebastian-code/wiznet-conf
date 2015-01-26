import time
import struct
import socket
import select
import logging
from optparse import OptionParser

logger = logging.getLogger("wiz1000")

WIZNET_OPERATION_MODES = {0x00: "client", 0x01: "server", 0x02: "mixed"}
WIZNET_PARITY = {0x00: "none", 0x01: "odd", 0x02: "even"}
WIZNET_FLOWCONTROL = {0x00: "none", 0x01: "xon/xoff", 0x02: "ctr/rts"}
WIZNET_IPCONFIGMODE = {0x00: "static", 0x01: "dhcp", 0x02: "pppoe"}
WIZNET_PROTOCOL = {0x00: "tcp", 0x01: "udp"}
WIZNET_BAUDRATES = {0xA0: 1200, 0xF4: 9600, 0xFE: 57600, 0xD0: 2400, 
                    0xFA: 19200, 0xFF: 115200, 0xE8: 4800, 0xFD: 38400, 
                    0xBB: 230400,
}

def hexdump(msg):
    return ' '.join(["%02x" % (ord(c),) for c in msg])

class S2E(object):
    """Represents a wiznet device"""
    _type = "Unknown"
    _basic_fields = [
        ("mac",                     "mac"),
        ("operation_mode",          "dictvalues", WIZNET_OPERATION_MODES),
        ("ip",                      "ip"),
        ("netmask",                 "ip"),
        ("gateway",                 "ip"),
        ("port",                    "short"),
        ("remote_ip",               "ip"),
        ("remote_port",             "short"),
        ("baudrate",                "dictvalues", WIZNET_BAUDRATES),
        ("databit",                 "byte"),
        ("parity",                  "dictvalues", WIZNET_PARITY),
        ("stop_bit",                "byte"),
        ("flow",                    "dictvalues", WIZNET_FLOWCONTROL),
        ("packing_byte",            "byte"),
        ("packing_length",          "short"),
        ("packing_interval",        "short"),
        ("tcp_timeout",             "short"),
        ("debug_enabled",           "bool", True),
        ("firmware_version",        "firmversion"),
        ("ip_config_mode",          "dictvalues", WIZNET_IPCONFIGMODE),
        ("ip_protocol",             "dictvalues", WIZNET_PROTOCOL),
        ("connected",               "bool", False),
        ("remote_use_dns",          "bool", False),
        ("dns_server",              "ip"),
        ("remote_host_dns",         "str", 32),
        ("serial_trigger_status",   "bool", False),
        ("serial_trigger_command",  "bytes", 3),
        ("pppoe_login",             "str", 32),
        ("pppoe_password",          "str", 32),
        ("wiznet_password_enabled", "bool", False),
        ("wiznet_password",         "str", 8, "%-8s"),
    ]
    _extended_fields = []
    UDP_LOCAL_PORT = None
    UDP_REMOTE_PORT = None

    def __init__(self, data=None):
        self._fields = self._basic_fields + self._extended_fields
        for field in self._fields:
            setattr(self, field[0], None)
        self.type = self._type
        self.data = data
        if self.data is not None:
            # Try to unpack
            self.unpack()

    def unpack(self):
        if self.data is not None:
            unpacker = Unpacker(self.data, pos=0)
            unpacker.unpack(self)

    def pack(self):
        packer = Packer()
        return packer.pack(self)

    def set_option(self, attr, value):
        if attr not in [f[0] for f in self._fields]:
            raise AttributeError("No such attribute '%s'" % (attr,))
        setattr(self, attr, value)

    def print_config(self):
        print "Config for %s" % (self,)
        for field in self._fields:
            print "\t%s='%s'" % (field[0], getattr(self, field[0], None))

    def __unicode__(self):
        return u"%(ip)s %(mac)s %(type)s v%(firmware_version)s" % self.__dict__

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class WIZ1x0SR(S2E):
    _type = "WIZ1x0SR"
    _extended_fields = []
    UDP_LOCAL_PORT = 5001
    UDP_REMOTE_PORT = 1460


class WIZ1000(S2E):
    _type = "WIZ1000"
    _extended_fields = [
        ("rfc2217_port",        "short"),
        ("rfc2217_password",    "str", 8, "%-8s"),
        ("search_password",     "str", 8, "%-8s"),
        ("keepalive_interval",  "short"),
        ("remote_ip_udp",       "ip"),
    ]
    UDP_LOCAL_PORT = 1138
    UDP_REMOTE_PORT = 5003