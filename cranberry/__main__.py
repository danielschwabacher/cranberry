import argparse
import os
import sys
import logging
from cranberry import cranberry

def main(args=None):
	"""Entry point for cranberry."""
	# If output and source flags are not specified -- use these
	DOWNLOAD_DIR = os.path.expanduser('~') + '/CranberryMusic/'
	SONGS_LOCATION = os.path.expanduser('~') + '/songsList.txt'
	DEFAULT_SENSOR = 'default'
	parser = argparse.ArgumentParser()
	parser.add_argument('-o',"--output-directory", default=DOWNLOAD_DIR, help='Specify directory to store downloaded files. Defaults to ~/CranberryMusic/')
	parser.add_argument('-s',"--source-file", default=SONGS_LOCATION, help='Specify plaintext that contains names of songs to download. Defaults to ~/songList.txt')
	parser.add_argument('-v', "--verbose", action="store_true", default=False, help='Enable verbose output, useful for debugging/development.')
	parser.add_argument('-q', "--quiet", action="store_true", default=False, help="Run in quiet mode, silences youtube-dl progress information.")
	parser.add_argument('-a', "--append-audio", action="store_true", default=False, help="Auto append audio to songs in song file, helps ensure the most accurate song match is found on Youtube.")
	parser.add_argument('-r', "--request-delay-time", type=int, default=0, help="Specify time between requests. Higher values may reduce the CAPTCHA issue error rate. Defaults to 0, no time between Youtube API request.")
	parser.add_argument('-d', "--display-session-info", action="store_true", help="Print information about Cranberry session arguments and then exit. Does NOT run a cranberry session")
	parser.add_argument('-x', "--sensor", default=DEFAULT_SENSOR, help="Advanced: specify a custom sensor to use during the parsing phase. Not yet implemented, option ignored.")
	args = parser.parse_args()
	args_dict = vars(args)
	if (args_dict['source_file'] == SONGS_LOCATION and args_dict['output_directory'] == DOWNLOAD_DIR and args_dict['sensor'] == DEFAULT_SENSOR):
		parser.print_help()
		exit(0)
	else:
		cranberry_main = cranberry.Cranberry(args_dict['output_directory'], args_dict['source_file'], args_dict['verbose'], args_dict['quiet'], args_dict['append_audio'], args_dict['request_delay_time'], args_dict['display_session_info'])
		cranberry_main.run()

if __name__ == "__main__":
	main()
