import argparse
import os
import sys
import logging
from cranberry import Cranberry

def main(args=None):
	"""Entry point for cranberry."""

	# If output and source flags are not specified -- use these
	DOWNLOAD_DIR = os.path.expanduser('~') + '/CranberryMusic'
	SONGS_LOCATION = os.path.expanduser('~') + '/songsList.txt'
	DEFAULT_SENSOR = 'default'

	parser = argparse.ArgumentParser()
	parser.add_argument('-o',"--output-directory", default=DOWNLOAD_DIR, help='Specify directory to store downloaded files. Defaults to ~/CranberryMusic/')
	parser.add_argument('-s',"--source-file", default=SONGS_LOCATION, help='Specify plaintext that contains names of songs to download. Defaults to ~/songList.txt')
	parser.add_argument('-v', "--verbose", action="store_true", default=False, help='Enable verbose output, useful for debugging/development.')
	parser.add_argument('-q', "--quiet", action="store_true", default=False, help="Run in quiet mode, silences youtube-dl progress information.")
	parser.add_argument('-x', "--sensor", default=DEFAULT_SENSOR, help="Advanced: specify a custom sensor to use during the parsing phase. Not yet implemented, option ignored.")
	args = parser.parse_args()
	args_dict = vars(args)

	cranberry_main = Cranberry.Cranberry(args_dict['output_directory'], args_dict['source_file'], args_dict['verbose'], args_dict['quiet'])
	cranberry_main.run()

if __name__ == "__main__":
	main()