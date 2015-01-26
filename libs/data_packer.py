class Packer(object):
    """Pack/Unpack data for WIZNet devices"""
    def pack(self, s2e):
        output = []
        for field in s2e._fields:
            name = field[0]
            packer = getattr(self, "pack_%s" % (field[1],))
            fieldvalue = getattr(s2e, name)
            packed = packer(fieldvalue, *field[2:])
            logger.debug("Packed %s %s -> `%s'" % (name, fieldvalue, packed))
            output.append(packed)
        return ''.join(output)

    def pack_ip(self, str_ip):
        """ip address should be in string form "1.2.3.4"""
        return struct.pack(">BBBB", *[ int(c) for c in str_ip.split(".") ])

    def pack_firmversion(self, version):
        return struct.pack(">BB", * [ int(c) for c in version.split(".") ])

    def pack_mac(self, str_mac):
        """mac address should be in string form "00:XX:22::FF:FF:FF"""
        return struct.pack(">BBBBBB", *[ int(c, 16) for c in str_mac.split(":") ])

    def pack_short(self, value):
        return struct.pack(">H", value)

    def pack_byte(self, value):
        return struct.pack(">B", int(value))

    def pack_bool(self, value, inverted=False):
        fmt = ">B"
        if inverted:
            value = not value
        if value:
            intval = 0x01
        else:
            intval = 0x00
        return struct.pack(fmt, intval)

    def pack_str(self, mystr, length, *args):
        fmt = "%(length)ss" % {"length": length }
        return struct.pack(fmt, mystr)

    def pack_dictvalues(self, value, dictvalues, *args):
        fmt = ">B"
        bytevalue = None
        for k, v in dictvalues.items():
            if v == value:
                bytevalue = k
                break
        assert(bytevalue is not None)
        return struct.pack(fmt, bytevalue)

    def pack_bytes(self, value, length):
        fmt = "B" * length
        return struct.pack(fmt, *[ int(x, 16) for x in value.split() ])