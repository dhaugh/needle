#!/bin/usr/env python
import pprint
import sys
import shutil
import subprocess
import plistlib

from util import plist_to_xml


def generate_metadat_dict(app_plist_file):  # -> dict()
    ''' Assumes that the input is the Info.plist file in the root directory of the ipa file after being unzipped '''
    return plist_to_xml(app_plist_file)[2]
#     plist_copy = '{}.xml.tmp'.format(app_plist_file)
#     shutil.copy2(app_plist_file, plist_copy)
#     cmd = ['plutil', '-convert', 'xml1', '{plist}'.format(plist=plist_copy)]
#     subprocess.call(cmd, shell=False)
#     xml_contents = open(plist_copy).read()
#     out = plistlib.readPlistFromString(xml_contents)
#     return out


#REFACTOR TO USE plist_to_xml
    

def run(app_plist_file):
    return generate_metadat_dict(app_plist_file)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: binary_metadata [binary_filepath]')
		sys.exit(1)
	out = dict(run(sys.argv[1]))
	pprint.pprint(out)
	print(type(out))
