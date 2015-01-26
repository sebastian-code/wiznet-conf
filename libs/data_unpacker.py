class Unpacker(object):
    """Helper class to unpack data received from WIZNet device"""
    def __init__(self, data, pos=0):
        self.data = data
        self.initialpos = self.pos = pos
    
    def unpack(self, s2e):
        self.pos = self.initialpos
        for field in s2e._fields:
            name = field[0]
            unpacker = getattr(self, "unpack_%s" % (field[1]), )
            unpacked = unpacker(*field[2:])
            logger.debug("Unpacked %s = %s" % (name, unpacked))
            setattr(s2e, name, unpacked)
        return s2e

    def unpack_ip(self):
        ip = struct.unpack(">BBBB", self.data[self.pos:self.pos + 4])
        self.pos += 4
        return ".".join(["%d" for x in xrange(4)]) % ip

    def unpack_firmversion(self):
        version = struct.unpack(">BB", self.data[self.pos:self.pos + 2])
        self.pos += 2
        return ".".join([ "%d" for x in xrange(2)]) % version

    def unpack_mac(self):
        mac = struct.unpack(">BBBBBB", self.data[self.pos:self.pos + 6])
        self.pos += 6
        return ":".join([ "%02x" for x in xrange(6)]) % mac

    def unpack_short(self):
        short = struct.unpack(">H", self.data[self.pos:self.pos + 2])[0]
        self.pos += 2
        return short

    def unpack_byte(self):
        byte = struct.unpack("B", self.data[self.pos])[0]
        self.pos += 1
        return byte

    def unpack_bytes(self, length):
        fmt = "B" * length
        outfmt = "0x%02x " * length
        bytes = struct.unpack(fmt, self.data[self.pos:self.pos + length])
        self.pos += length
        return outfmt % bytes

    def unpack_bool(self, inverted=False):
        fmt = "B"
        b = bool(struct.unpack(fmt, self.data[self.pos])[0])
        self.pos += 1
        if inverted:
            return not b
        else:
            return b
    
    def unpack_str(self, length, outfmt="%s"):
        fmt = ">%(length)ss" % {"length": length}
        value = struct.unpack(fmt, self.data[self.pos:self.pos + length])[0]
        self.pos += length
        return outfmt % (value,)
    
    def unpack_dictvalues(self, dictvalues, default=None):
        """1 Byte of data to dict value"""
        fmt = "B"
        key = struct.unpack(fmt, self.data[self.pos])[0]
        self.pos += 1
        return dictvalues.get(key, default)