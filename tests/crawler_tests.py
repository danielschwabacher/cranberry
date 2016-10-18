import unittest
from cranberry import crawler

class Crawler_Tests(unittest.TestCase):
    def object_create(self):
        test_crawler = crawler.Crawler("test", "test")
        self.assertEqual(1, 2, 'test_crawler is not a crawler object')

tester = Crawler_Tests()
tester.object_create()
