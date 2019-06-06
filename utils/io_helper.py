import struct


class IOHelper:
    @staticmethod
    def read_format(io, format):
        size = struct.calcsize(format)
        buffer = io.read(size)
        data = struct.unpack(format, buffer)
        return data

    @staticmethod
    def read_string(io, size, encoding='utf8'):
        buffer = io.read(size)  # type: bytes
        string = buffer.decode(encoding)
        return string

    @staticmethod
    def peek(io, size):
        o = io.tell()
        buffer = io.read(size)
        io.seek(o)
        return buffer
