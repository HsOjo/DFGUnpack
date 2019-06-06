import json
import os
import sys

from common import write_file
from models.dfg_assets import DFGAssets
from models.dfg_pack import DFGPack

DIR_EXTRACT = './output'


def extract_assets(path, folder_ex):
    a = DFGAssets()
    a.load(path)
    for f in a.assets:
        write_file('%s/%s' % (folder_ex, f['name']), f['data'])


def extract_packs(folder):
    for f in os.listdir(folder):
        if f[-4:] == '.pak':
            p = DFGPack()
            p.load('%s/%s' % (folder, f))

            d = '%s/packs/%s' % (folder, f)
            os.makedirs(d)

            for i, v in enumerate(p.files):
                write_file('%s/%s.png' % (d, i), v['data'])

            with open('%s/info.json' % d, 'w') as io:
                json.dump([{'x': i['x'], 'y': i['y']} for i in p.files], io, indent=4)


os.makedirs(DIR_EXTRACT, exist_ok=True)
path = ' '.join(sys.argv[1:])
print(path)
extract_assets(path, DIR_EXTRACT)
extract_packs(DIR_EXTRACT)
