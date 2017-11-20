#from urllib import request
import requests
import urllib.parse
import re
import logging
import time
import random
from fake_useragent import UserAgent

class URL_Creator():
	""" The URL_Creator class is used to transform the song-list created by Linter into
	a form usable by the youtube-dl Uploader. It handles stuff like the URL transformations. """
	def __init__(self, linted_list):
		self.songs_list = linted_list
		self.cranberry_fake_headers = {
    		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		}

	def update_headers(self):
		ua = UserAgent()
		self.cranberry_fake_headers['User-Agent'] = ua.random
		logging.debug("Headers are: " + str(self.cranberry_fake_headers))

	def create_urls(self, delay_time):
		list_of_urls = []
		for item in self.songs_list:
			print("Getting url for song: ", item)
			self.update_headers()
			# Sleep between API requests, hopefully reduces CAPTCHA errors.
			time.sleep(delay_time)
			html_content = requests.get("http://www.youtube.com/results?search_query=" + item, headers=self.cranberry_fake_headers)
			try:
				search_results = re.findall(r'\/watch\?v=(.{11})', html_content.content.decode('utf-8'))	
				logging.debug("Search results are: " + str(search_results))
				if html_content.status_code == 503:
					print("CAPTCHA Error, cranberry cannot continue. Run with -v for more information. Cranberry will now exit.")
					logging.debug("Status code: ", html_content.status_code)
					logging.debug("Text response: ", html_content.text)
					logging.debug("Youtube has detected that we have requested too many resources. This usually happens when you try to download many songs in a short period of time.")
					logging.debug("To fix this, you can manually complete the CAPTCHA on Youtube, or you can wait a bit and try using cranberry again.")
					exit(-1)
				url_string = "http://www.youtube.com/watch?v=" + search_results[0]
				list_of_urls.append(url_string)
			except Exception as e:
				print("Unknown error, skipping: " + str(item))
				print("Exception was: " + str(e))
		return list_of_urls
