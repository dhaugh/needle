#!/usr/bin/env python
import pprint
import subprocess
import sys

from util import plist_to_xml


def find_all_plists(root_dir):
    cmd = ['find', root_dir, '-type', 'f', '-name', '*.plist']
    out = subprocess.check_output(cmd)
    plist_files = out.split('\n')
    plist_files = filter(None, plist_files)
    return plist_files


def run(root_dir):
    return find_all_plists(root_dir)


def all_plist_files_as_xml(root_dir):  # -> [(new_xml_filepath, new_xml_contents)...]
    ''' creates xml versions of the existing plist files, and returns the new file path and contents as a str'''
    out = []
    all_plist_files = find_all_plists(root_dir)
    for plist in all_plist_files:
    	new_fp, new_contents, new_content_dict = plist_to_xml(plist)
    	out.append((new_fp, new_contents))
    return out


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: storage_files_plist.py [root_dir_of_dump]')
		sys.exit(1)
# 	pprint.pprint(run(sys.argv[1]))
	pprint.pprint(all_plist_files_as_xml(sys.argv[1]))
