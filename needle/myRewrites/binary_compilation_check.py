#!/usr/bin/env python
import subprocess
import sys
import re


def run_otool(query, binary_file, grep=None):
    """Run otool against a specific architecture."""
    otool_cmd = ['otool', query, binary_file]
    if grep:
    	grep_cmd = ['grep', '-Ei', grep]
    	otool_proc = subprocess.Popen(otool_cmd, stdout=subprocess.PIPE, shell=False)
    	grep_proc = subprocess.Popen(grep_cmd, stdin=otool_proc.stdout, stdout=subprocess.PIPE, shell=False)
    	return grep_proc.communicate()[0]
    else:
        return subprocess.check_output(otool_cmd)
     

def check_flag(line, testname, flag):
    """Extract result of the test."""
    tst = filter(lambda el: re.search(flag, el), line)
    res = True if tst and len(tst) > 0 else False
    return testname, res


# ==================================================================================================================
# CHECKS
# ==================================================================================================================
def check_cryptid(binary_filepath):
    out = run_otool('-l', binary_filepath, grep='cryptid')
    return check_flag(out, "Encrypted", "cryptid(\s)+1")


def check_pie(binary_filepath):
    out = run_otool('-hv', binary_filepath)
    return check_flag(out, "PIE", "PIE")


def check_arc(binary_filepath):
    out = run_otool('-IV', binary_filepath, grep='(\(architecture|objc_release)')
    return check_flag(out, "ARC", "_objc_release")

def check_stack_canaries(binary_filepath):
    out = run_otool('-IV', binary_filepath, grep='(\(architecture|___stack_chk_(fail|guard))')
    return check_flag(out, "Stack Canaries", "___stack_chk_")


def run(binary_file_path):  # -> [(Test name, Test passed)...]
    testname_result_tups = map(lambda f: f(binary_file_path), [check_cryptid, check_pie, check_arc, check_stack_canaries])
    print(testname_result_tups)


if __name__ == '__main__': 
	if len(sys.argv) != 2:
		print('usage: binary_compilation_check.py [ios binary]') 
		sys.exit(1)
	run(sys.argv[1])
