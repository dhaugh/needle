import subprocess


def find_otool():
    return subprocess.check_output('which otool', shell=True).strip()


if __name__ == '__main__':
	print('otool is at {}'.format(find_otool()))
