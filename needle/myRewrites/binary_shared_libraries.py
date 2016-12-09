import sys
import subprocess

from find_tools import find_otool

def run(binary_filepath):
    cmd = [find_otool(), '-L', binary_filepath]
    out = subprocess.check_output(cmd)
    out = out.split('\n\t')
    print(out)
    out = map(lambda x: x.strip(), out)
    return out


if __name__ == '__main__':
	print(sys.argv)
	if len(sys.argv) != 2:
		print('usage: binary_shared_libraries [binary_filepath]')
		sys.exit(1)
	run(sys.argv[1])
