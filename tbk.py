#! /usr/bin/env python

"""
Retrun: Random a File
"""

import os
import random

class RAF(object):
	def __init__(self, *url):
		self.url = url
		self.filelist = [os.listdir(x) for x in url]

	def get_filelist(self):
		for lst in self.filelist:
			for elm in lst:
				print elm

	def get_a_file(self):
		return random.choice(random.choice(self.filelist))


if __name__ == "__main__":
	raf = RAF("/home/factpass/Music/free/environment/", "/home/factpass/Music/free/japanese/")
#raf.get_filelist()
	print raf.get_a_file()
