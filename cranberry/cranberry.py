import argparse
import sys
from cranberry import linter
from cranberry import crawler
from cranberry import youtubeparser
from cranberry import uploader
from cranberry import sensor
import os
import logging

class Cranberry():
	""" Cranberry objects are responsible for starting, managing, monitoring 
	and terminating the various processes necessary to facilitate a successful
	Cranberry run. They basically coordinate the entire program and can 
	also be thought of as runners. Cranberry objects delegate the bulk of their 
	work to other modules (filesystem, parser, uploader, etc.) to do the associative task. 
	There should not be more than one of these objects in any given program using Cranberry. """
	def __init__(self, dl_dir, songs_loc, verbose, quiet):
		self.dl_dir = dl_dir
		self.songs_loc = songs_loc
		self.verbose = verbose
		if (self.verbose):
			logging.basicConfig(level=logging.DEBUG)
			logging.debug("You are in debugging mode.")
		self.quiet = quiet
		self.sensor = sensor

	def print_args(self):
		print("Download dir: ", self.dl_dir)
		print("Source File: ", self.songs_loc)

	def run(self):
		print("---WELCOME TO CRANBERRY---")
		filesystem_crawler = crawler.Crawler(self.dl_dir, self.songs_loc)
		filesystem_crawler.operations_runner(self.dl_dir, self.songs_loc)
		# ~~~~~~~~~~
		song_file_parser = linter.Linter(self.songs_loc)
		final_songs_list = song_file_parser.create_final_list(self.songs_loc)
		# ~~~~~~~~~~
		yt_parser = youtubeparser.Youtube_Parser(final_songs_list)
		url_list = yt_parser.create_urls()
		# ~~~~~~~~~~
		main_uploader = uploader.Uploader(url_list, self.dl_dir, self.quiet)
		main_uploader.process_all_urls()
		print("Done!")
		# ~~~~~~~~~~
		print("---CRANBERRY SESSION OVER---")
		exit(0)

