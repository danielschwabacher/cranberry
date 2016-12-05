import unittest
from cranberry import crawler

class TestCrawler(unittest.TestCase):
	def test_output_dir_validation(self):
		test_crawler = crawler.Crawler("outputDir", "test")
		self.assertEqual(test_crawler.output_directory, "outputDir", "FAILED -- output dir assignment in Crawler.")
	def test_song_file_validation(self):
		test_crawler = crawler.Crawler("test", "songFileLocation")
		self.assertEqual(test_crawler.song_loc, "songFileLocation", "FAILED -- song file assignment in Crawler.")

if __name__ == '__main__':
	unittest.main()
