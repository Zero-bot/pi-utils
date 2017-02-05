#!/usr/bin/python
import os 
import glob
from subprocess import call
from subprocess import call
import sys
from random import shuffle

path ='/media/Backup/songs/Alai Payuthe/'
_shuffle = False
if len(sys.argv) == 2:
		path = sys.argv[1]
if len(sys.argv) == 3:
	if sys.argv[1]=='-s':
		_shuffle = True
		path = sys.argv[2]
	else:
		print("Invalid args")
		sys.exit(0)
def get_files():
	ext = ('/*.mp3', '/*.mp4', '/*.avi')
	multimedia_files =[]
	for types in ext:
		multimedia_files.extend(glob.glob(path+types))
	return multimedia_files

def play_files_dir( multimedia_files):
	for files in multimedia_files:
		try:
			call (['omxplayer', files])
		except KeyboardInterrupt,Exception:
			print("# Received Keyboard Interrupt")
			return

def start_player():
	media_files = get_files()
	if _shuffle:
		shuffle(media_files)
	play_files_dir(media_files)

if __name__ == "__main__":
	start_player()
