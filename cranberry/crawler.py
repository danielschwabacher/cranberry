import os
import logging
# TODO: add helpers (get ouput_dir, get song_loc)
class Crawler():
	""" Crawler objects are used to observe and, if nessecary, create the relevant
	filesystem paths so that Cranberry can run successfully. """
	def __init__(self, dir_c, file_c):
		self.output_directory = dir_c
		self.song_loc = file_c

	def validate_ouput_dir(self):
		if (os.path.exists(self.output_directory) == True):
			return 0
		else:
			logging.debug("The output directory does not exist, creating it...")
			self.create_output_dir(self.output_directory)

	def validate_song_file(self):
		if (os.path.exists(self.song_loc)):
			return 0
		else:
			print("Song file does not exist, create the song file before continuing.")
			logging.debug("Song file {0} does not exist, you must create it before continuing".format(self.song_loc))
			exit(-1)
			
	def create_output_dir(self):
		try:
			os.mkdir(self.output_directory)
		except:
			logging.debug("Error creating directory at: ", self.output_directory)
			exit(-1)

	# keep Cranberry objects clean by implementing logic in one function within Crawler
	def operations_runner(self):
		self.validate_ouput_dir()
		self.validate_song_file()

