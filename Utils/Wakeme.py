#!/usr/bin/python
import datetime
import time
import os 
from os.path import isfile, join
from subprocess import call
import glob
from random import shuffle

folder = '/media/HP v215b/'
alarm_time = [22,47]
if os.path.exists(folder):
	folder = folder+"*.mp4"
else:
	folder = "/home/pi/Desktop/*.mp4"

def sleep_for(hour,minute=0):
	today7am = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
	now = datetime.datetime.now()
	if today7am >= now:
		return (today7am-now).seconds-1
	else:
		return 86439-(now-today7am).seconds 

def play_my_song(song):
	return call (['omxplayer', song])

def wakeme():
	while True:
		sleep = sleep_for(alarm_time[0],alarm_time[1])
		player = None
		print("# Sleeping for %d hours %d minutes %d seconds" %(sleep/60/60, sleep/60%60, sleep%60))
		time.sleep(sleep)		
		try:
			play_files_dir()
		except KeyboardInterrupt,Exception:
			print("# Received Keyboard Interrupt")
			continue

def play_files_dir():
	videos = glob.glob(folder)
	shuffle(videos)
	for files in videos:
		play_my_song(files)
		
if __name__ == "__main__":
	wakeme()
