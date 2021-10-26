import os, sys

scriptsFolder = os.path.dirname(os.path.realpath(__file__)) + '/scripts'

def argsToString(args):
    nargs = []
    for arg in arg:
        if ' ' in str(arg):
            nargs.append('"{}"'.formart(str(arg)))
        else:
            nargs.append(str(arg))
    
    return ' '.join(nargs)

try:
    script = sys.argv[1]
except:
    script = 'list'

os.system(f'bash {scriptsFolder}/{script}.sh')