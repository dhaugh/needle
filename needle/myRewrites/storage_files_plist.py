#!/usr/bin/env python
import pprint
import subprocess
import sys


def find_all_plists(root_dir):
    cmd = ['find', root_dir, '-type', 'f', '-name', '*.plist']
    out = subprocess.check_output(cmd)
    plist_files = out.split('\n')
    return plist_files


def run(root_dir):
    return find_all_plists(root_dir)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: storage_files_plist.py [root_dir_of_dump]')
		sys.exit(1)
	pprint.pprint(run(sys.argv[1]))
