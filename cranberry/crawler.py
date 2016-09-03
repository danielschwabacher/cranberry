import os
import logging
# TODO: add helpers (get ouput_dir, get song_loc)
class Crawler():
	""" Crawler objects are used to observe and, if nessecary, create the relevant 
	filesystem paths so that Cranberry can run successfully. """
	def __init__(self, dir_c, file_c):
		self.output_directory = dir_c
		self.song_loc = file_c
	def validate_ouput_dir(self, dir_c):
		if (os.path.exists(dir_c) == True):
			return 0
		else:
			logging.debug("The output directory does not exist, creating it...")
			self.create_output_dir(self.output_directory)
	def validate_song_file(self, file_c):
		if (os.path.exists(file_c) == True):
			return 0
		else: 
			logging.debug("Song file does not exists, create a song file before continuing.")

	def create_output_dir(self, dir_c):
		try:
			os.mkdir(dir_c)
		except:
			logging.debug("Error creating directory at: ", dir_c)

	# keep Cranberry objects clean by implementing logic in one function within Crawler
	def operations_runner(self, dir_c, file_c):
		try:
			self.validate_ouput_dir(self.output_directory)
			self.validate_song_file(self.song_loc)
		except:
			logging.debug("Filesystem checks failed")
