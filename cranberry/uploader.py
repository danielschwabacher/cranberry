from __future__ import unicode_literals
import youtube_dl
import os
import logging

class BaseLogger(object):
    def debug(self, msg):
        logging.debug(msg)

    def warning(self, msg):
        logging.debug(msg)

    def error(self, msg):
        logging.debug(msg)


class Uploader():
    """ The uploader class wraps around youtube-dl with the goal of 
    providing an easy-to-use interface for calling youtube-dl within 
    Cranberry. 
    Process (seen in the functions below), in the following context, means to:
    1.) Upload to youtube-dl.
    2.) Download using youtube-dl.
    """
    def __init__(self, resource_list, directory, quiet):
        self.url_list = resource_list
        self.full_directory_path = directory + '/'
        self.output = '{}{}'.format(self.full_directory_path, '%(title)s.%(ext)s')
        self.template = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': self.output
        }
        if (quiet):
            self.template['quiet'] = True

    # upload a single url to youtube-dl 
    def process_single_url(self, single_url):
        with youtube_dl.YoutubeDL(self.template) as ydl:
            ydl.download(single_url)

    # upload all urls in the url_list to youtube-dl for processing. 
    # The url_list is the one provided to the Uploader constructor. 
    def process_all_urls(self):
        with youtube_dl.YoutubeDL(self.template) as ydl:
        #logging.debug("in uploader -- downloading: %s", resource)
            logging.debug("template is: %s", self.template)
            ydl.download(self.url_list)