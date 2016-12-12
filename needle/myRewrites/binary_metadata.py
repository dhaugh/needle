#!/bin/usr/env python
import pprint
import sys
import shutil
import subprocess
import plistlib


def generate_metadat_dict(app_plist_file):
    pass
    '''
    Assumes that the input is the Info.plist file in the root directory of the ipa file after being unzipped
    '''
    plist_copy = '{}.xml.tmp'.format(app_plist_file)
    shutil.copy2(app_plist_file, plist_copy)
    cmd = ['plutil', '-convert', 'xml1', '{plist}'.format(plist=plist_copy)]
    subprocess.call(cmd, shell=False)
    xml_contents = open(plist_copy).read()
    out = plistlib.readPlistFromString(xml_contents)
    return out
    

def run(app_plist_file):
    return generate_metadat_dict(app_plist_file)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: binary_metadata [binary_filepath]')
		sys.exit(1)
	out = run(sys.argv[1])
	pprint.pprint(out)
