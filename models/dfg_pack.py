from io import BytesIO, SEEK_END

from utils.io_helper import IOHelper


class DFGPack:
    def __init__(self):
        self._io = None  # type: BytesIO
        self.files = []

    def load(self, path):
        self._io = open(path, 'rb')
        self._io.seek(0, SEEK_END)
        ep = self._io.tell()
        self._io.seek(2)

        while self._io.tell() < ep:
            [x, y, size] = IOHelper.read_format(self._io, '<2hi')
            data = self._io.read(size)
            self.files.append({
                'x': x,
                'y': y,
                'size': size,
                'data': data,
            })
