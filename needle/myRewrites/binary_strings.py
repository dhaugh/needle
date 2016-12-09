import sys
import subprocess

min_length = 10
query_strings = ['https://', 'http://', 'ViewController']


def run_string_analysis(binary_filepath, min_length=10, query=query_strings):
#     cmd = '''strings "{app}" | awk 'length > {length}' | sort -u | grep -E '{query}' '''.format(app=binary_filepath, length=min_length, query=query)
    query_str = '({})'.format('|'.join(query))
    strings_cmd = ['strings', binary_filepath]
    strings_proc = subprocess.Popen(strings_cmd, stdout=subprocess.PIPE, shell=False)
    awk_cmd = ['awk', 'length > {}'.format(min_length)]
    awk_proc = subprocess.Popen(awk_cmd, stdout=subprocess.PIPE, stdin=strings_proc.stdout, shell=False)
    sort_cmd = ['sort', '-u']
    sort_proc = subprocess.Popen(sort_cmd, stdout=subprocess.PIPE, stdin=awk_proc.stdout, shell=False)
    grep_cmd = ['grep', '-E', query_str]
    grep_proc = subprocess.Popen(grep_cmd, stdout=subprocess.PIPE, stdin=sort_proc.stdout, shell=False)
    out = grep_proc.communicate()[0]
    out = out.split('\n')
    return out


def run(binary_filepath):
    return run_string_analysis(binary_filepath)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage: binary_strings.py [binary_filepath]')
		sys.exit(1)
	print(run(sys.argv[1]))
