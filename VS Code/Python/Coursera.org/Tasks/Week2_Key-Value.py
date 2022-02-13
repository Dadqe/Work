# storage.py
# Так должна называться утилита... имя файла?

import argparse
import json
import os
import tempfile


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()

if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
