class WizSearch(object):
    DEVICE_TYPES = {
        "wiz1000": WIZ1000,
        "wiz1x0sr": WIZ1x0SR,
    }

    def __init__(self, address="192.168.11.255",
                 broadcast=False,
                 bind_address="0.0.0.0",
                 device_type="wiz1000",
                 allowed_mac=None,
                 search_password="wiznet", timeout=2.0):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        if broadcast:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        s.bind((
            bind_address,
            WizSearch.DEVICE_TYPES[device_type].UDP_LOCAL_PORT,
        ))
        self.device_s = s

        self.search_password = search_password
        self.timeout = timeout
        self.address = (
            address,
            WizSearch.DEVICE_TYPES[device_type].UDP_REMOTE_PORT,
        )
        self.device_type = device_type
        self._devices_list = []
        self.allowed_mac = allowed_mac or []
        self.broadcast = broadcast

    def sendto(self, data):
        logger.debug("sendto %s" % (data[:4],))
        self.device_s.sendto(data, self.address)

    def recvfrom(self, size=1500):
        data, addr = self.device_s.recvfrom(size)
        if not self.broadcast and addr != self.address:
            raise WizSearchException(
                "Unexpected packet recevied from %s, expected was %s" % (
                    addr, self.address))
        logger.debug("recvfrom: %s" % (data[:4]))
        return data

    def get_devices(self):
        devices = {}
        for device in self._devices_list:
            if device.mac in devices:
                raise WizSearchException(
                    "Multiple devices found with mac '%s'" % (
                        device.mac,
                    ))
            devices[device.mac] = device
        return devices

    def update(self):
        """
        Search devices. timeout is expressed in seconds.
        """
        self._devices_list = []
        self.sendto("FIND%-8s" % (self.search_password,))

        start = time.time()
        while start + self.timeout > time.time():
            rfds, _, _ = select.select([self.device_s], [], [], 0.5)

            for sock in rfds:
                data = self.recvfrom()
                if data[0:4] in ("IMIN", "SETC"):
                    try:
                        dev = WizSearch.DEVICE_TYPES[self.device_type](data[4:])
                        # devices.append(self.extract_IMIN(data, wiztype))
                        if not self.allowed_mac or dev.mac in self.allowed_mac:
                            self._devices_list.append(dev)
                    except:
                        logger.exception("parsing error.")

        if not self._devices_list:
            logger.error("Timeout, no devices found")
        return self._devices_list

    def send_config(self, device):
        data = device.pack()
        self.sendto("SETT%s" % (data,))
        ack = self.recvfrom()
        if ack[:4] != "SETC":
            logger.error("Unexpected data '%s'" % (data[:4]))
        if ack[4:] != data:
            logger.error("ACK failed")
        else:
            logger.debug("ACK sucess")

    def set_options(self, **kwargs):
        devices = self.get_devices()
        for dev in devices.values():
            for opt, val in kwargs.items():
                dev.set_option(opt, val)
            if kwargs:
                self.send_config(dev)
            else:
                dev.print_config()

    @staticmethod
    def main():
        parser = OptionParser()
        parser.add_option(
            "-b", dest="broadcast_address",
            action="store",
            help="Broadcast address",
        )
        parser.add_option(
            "-a", dest="address",
            help="Device IP address",
        )
        parser.add_option(
            "--device-type",
            choices=["wiz1000", "wiz1x0sr"],
            default="wiz1000",
            help="Device type",
        )
        parser.add_option(
            "-m", dest="mac_list",
            help="Limit actions to theses mac address",
        )
        parser.add_option(
            "-s", dest="device_search_password",
            default="wiznet",
            help="Search password",
        )

        # Generate options based on fields descriptions
        fields = WIZ1000._basic_fields + WIZ1000._extended_fields
        for field in fields:
            option = "--%s" % (field[0].replace("_", "-"),)
            kwargs = {}
            if field[1] == "bool":
                kwargs["action"] = "store_true"
            if field[1] == "short":
                kwargs["type"] = "int"
            if field[1] == "dictvalues":
                choices = field[2].values()
                if isinstance(choices[0], int):
                    kwargs["type"] = "int"
                else:
                    kwargs["choices"] = choices
                kwargs["help"] = ",".join(["%s" % (v,) for v in choices])
            parser.add_option(option, dest=field[0], **kwargs)
            if field[1] == "bool":
                # For boolean field, add --no-option
                kwargs["action"] = "store_false"
                parser.add_option("--no-%s" % (field[0].replace("_", "-"),),
                                  dest=field[0], **kwargs)
        options, _ = parser.parse_args()

        kwargs = {}
        for field in fields:
            value = getattr(options, field[0])
            if value is not None:
                kwargs[field[0]] = value

        search_kwargs = {
            "broadcast": True,
            "address": "192.168.11.255",
            "device_type": options.device_type,
            "search_password": options.device_search_password,
        }
        if options.mac_list:
            search_kwargs["allowed_mac"] = options.mac_list.split(',')
        if options.broadcast_address:
            search_kwargs["address"] = options.broadcast_address
        if options.address:
            search_kwargs["address"] = options.address
            search_kwargs["broadcast"] = False
        searcher = WizSearch(**search_kwargs)
        searcher.update()
        searcher.set_options(**kwargs)