import zlib
from io import BytesIO

from utils.io_helper import IOHelper


class DFGAssets:
    def __init__(self):
        self._io = None  # type: BytesIO
        self.assets = []

    def load(self, path):
        self._io = open(path, 'rb')
        is_zip = IOHelper.peek(self._io, 1) == b'\x01'
        if is_zip:
            self._io.seek(1)

        self.assets.clear()
        [file_num] = IOHelper.read_format(self._io, '<i')
        for _ in range(file_num):
            [name_size] = IOHelper.read_format(self._io, '<i')
            name = IOHelper.read_string(self._io, name_size)

            if is_zip:
                [size_raw, size_zip] = IOHelper.read_format(self._io, '<2i')

                self.assets.append({
                    'name': name,
                    'size_raw': size_raw,
                    'size_zip': size_zip,
                    'data': None,
                })
            else:
                [size] = IOHelper.read_format(self._io, '<i')

                self.assets.append({
                    'name': name,
                    'size': size,
                    'data': None,
                })

        for i in range(file_num):
            a = self.assets[i]
            if is_zip:
                a['data'] = self._io.read(a['size_zip'])
                a['data'] = zlib.decompress(a['data'])
            else:
                a['data'] = self._io.read(a['size'])
