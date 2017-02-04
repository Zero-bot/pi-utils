#!/usr/bin/python

import subprocess
import re

def get_dev_name():
	return str(re.search('(\/dev\/sd[a-z]\d{1}):\sLABEL=\"Media\"', str(subprocess.Popen(['blkid'], stdout=subprocess.PIPE).communicate())).group(1))

def mount_media_partition_from_hdd():
	err = subprocess.Popen(['mount', get_dev_name(), '/media/media'], stderr=subprocess.PIPE, stdout=subprocess.PIPE).stderr.read()
	if len(err) is 0:
		print("# Media partition in HDD mounted succesfully")
	else:
		print("# Failed to mount media partition")
		print(err)
	

if __name__ == "__main__":
	mount_media_partition_from_hdd()
