import shutil
import subprocess
import plistlib


def plist_to_xml(plist_filepath):  # -> (filepath_of_new_xml_file, contents_of_new_file, xml_contents_as_dict)
    '''
    creates an xml version of a plist file in the same directory named <filename>.xml.tmp
    returns the new filepath and the contents of the new file
    ensure that the file exists prior to calling this function
    '''
    new_xml_filepath = '{}.xml.tmp'.format(plist_filepath)
    shutil.copy2(plist_filepath, new_xml_filepath)
    cmd = ['plutil', '-convert', 'xml1', '{plist}'.format(plist=new_xml_filepath)]
    subprocess.call(cmd, shell=False)
    xml_contents = open(new_xml_filepath).read()
    xml_contents_as_dict = plistlib.readPlistFromString(xml_contents)
    return new_xml_filepath, xml_contents, xml_contents_as_dict


def find_file(root_dir, regex):  # -> [filepath_string]
    cmd = ['find', root_dir, '-type', 'f', '-name', regex]
    out = subprocess.check_output(cmd)
    out = out.split('\n')
    out = filter(None, out)
    return out
