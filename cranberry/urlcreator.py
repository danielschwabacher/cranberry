from urllib import request
import urllib.parse
import re
import logging

class URL_Creator():
	""" The URL_Creator class is used to transform the song-list created by Linter into
	a form usable by the youtube-dl Uploader. It handles stuff like the URL transformations. """
	def __init__(self, linted_list):
		self.songs_list = linted_list

	def create_urls(self):
		list_of_urls = []
		for item in self.songs_list:
			logging.debug("Getting url for song: %s", item)
			html_content = urllib.request.urlopen("http://www.youtube.com/results?search_query=" + item)
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
			url_string = "http://www.youtube.com/watch?v=" + search_results[0]
			list_of_urls.append(url_string)
		return list_of_urls
