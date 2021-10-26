import sys, os, shutil

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open('ttools', 'w') as f:
    f.write(f'#!/bin/bash\npython3 "{filesFolder}/.run.py" "$@"')