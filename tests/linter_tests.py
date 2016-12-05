import unittest
from cranberry import linter

class TestLinter(unittest.TestCase):
	def test_create_song_list(self):
		expected_output_appended = ['test1 audio\n', 'test2 spaces audio\n', 'test3_underscores audio\n']
		expected_output_no_append = ['test1\n', 'test2 spaces\n', 'test3_underscores\n']
		source_file = "test_data.txt"
		test_append_linter = linter.Linter(source_file, True)
		self.assertEqual(expected_output_appended, test_append_linter.create_songs_list(source_file))
		test_linter = linter.Linter(source_file, False)
		self.assertEqual(expected_output_no_append, test_linter.create_songs_list(source_file))
	def test_add_query_compatiblity(self):
		pass
	def test_create_final_list(self):
		pass

if __name__ == '__main__':
	unittest.main()
