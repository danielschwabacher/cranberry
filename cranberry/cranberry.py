import argparse
import sys
from cranberry import linter
from cranberry import crawler
from cranberry import urlcreator
from cranberry import uploader
from cranberry import sensor
import os
import logging
import time

class Cranberry():
	""" Cranberry objects are responsible for starting, managing, monitoring
	and terminating the various processes necessary to facilitate a successful
	Cranberry run. They basically coordinate the entire program and can
	also be thought of as runners. Cranberry objects delegate the bulk of their
	work to other modules (filesystem, parser, uploader, etc.) to do the associative task.
	There should not be more than one of these objects in any given program using Cranberry. """
	def __init__(self, dl_dir, songs_loc, verbose, quiet, auto_append, time, display_info_exit):
		self.dl_dir = dl_dir
		self.songs_loc = songs_loc
		self.verbose = verbose
		if (self.verbose):
			logging.basicConfig(level=logging.DEBUG)
			logging.debug("You are in debugging mode.")
		self.quiet = quiet
		self.sensor = sensor
		self.auto_append = auto_append
		self.request_delay_time = time
		self.show_and_exit = display_info_exit

	def print_args(self):
		print("Download dir: ", self.dl_dir)
		print("Source File: ", self.songs_loc)

	def run(self):
		if (self.show_and_exit):
			# Only display cranberry session info, then exit.
			print("-----Cranberry Session Info-----")
			print("1.) Output directory: " + str(self.dl_dir))
			print("2.) Song file: " + str(self.songs_loc))
			print("3.) Quiet mode: " + str(self.quiet))
			print("4.) Sensor: " + str(self.sensor))
			print("5.) Append Audio: " + str(self.auto_append))
			print("6.) Request Delay Time: " + str(self.request_delay_time))
			exit(0)
		# ~~~~~~~~~~
		print("----------Cranberry Session Started at: {0}----------".format(time.ctime()))
		filesystem_crawler = crawler.Crawler(self.dl_dir, self.songs_loc)
		filesystem_crawler.operations_runner()
		if (self.auto_append == True):
			song_file_parser = linter.Linter(self.songs_loc, True)
			final_songs_list = song_file_parser.create_final_list()
		else:
			song_file_parser = linter.Linter(self.songs_loc, False)
			final_songs_list = song_file_parser.create_final_list()
		# ~~~~~~~~~~
		url_transformer = urlcreator.URL_Creator(final_songs_list)
		url_list = url_transformer.create_urls(self.request_delay_time)
		# ~~~~~~~~~~
		main_uploader = uploader.Uploader(url_list, self.dl_dir, self.quiet)
		main_uploader.process_all_urls()
		print("Done!")
		# ~~~~~~~~~~
		print("---CRANBERRY SESSION OVER---")
		exit(0)
