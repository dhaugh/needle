#!/bin/usr/env python
import pprint
import sys
import subprocess
import shutil

from util import find_file


def find_sql_files(root_dir):  # -> [db_filepath<str>, ...]
    return find_file(root_dir, '*sql*')


def find_db_schema(sqlite_db_filepath):  # -> str
    cmd = ['sqlite3', sqlite_db_filepath, '.schema']
    out = subprocess.check_output(cmd)
#     out = out.split('\n')
    return out


def run(root_dir):  # -> [(db_filepath<str>, db_schema<str>) ...]
    sql_files = find_sql_files(root_dir)
    out = map(lambda db_fp: (db_fp, find_db_schema(db_fp)), sql_files) 
    return out


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: storage_files_sql.py [root_dir]')
		sys.exit(1)
	out = run(sys.argv[1])
	print(out)
