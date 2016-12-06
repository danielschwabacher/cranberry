import unittest
from cranberry import linter

class TestLinter(unittest.TestCase):
	source_file = "test_data.txt"
	test_append_linter = linter.Linter(source_file, True)
	test_linter = linter.Linter(source_file, False)
	def test_create_song_list(self):
		expected_output_appended = ['test1 audio\n', 'test2 spaces audio\n', 'test3_underscores audio\n']
		expected_output_no_append = ['test1\n', 'test2 spaces\n', 'test3_underscores\n']
		self.assertEqual(expected_output_appended, self.test_append_linter.create_songs_list())
		self.assertEqual(expected_output_no_append, self.test_linter.create_songs_list())
	def test_add_query_compatiblity(self):
		expected_query_output = ['test1\n', 'test2+spaces\n', 'test3_underscores\n']
		with open(self.source_file) as testing_file:
			self.assertEqual(expected_query_output, self.test_append_linter.add_query_compatibility(testing_file))
	def test_create_final_list(self):
		expected_final_list_output = ['test', 'test+spaces', 'testunderscores']
		expected_final_list_appended = ['test+audio','test+spaces+audio', 'testunderscores+audio']
		self.assertEqual(expected_final_list_output, self.test_linter.create_final_list())
		self.assertEqual(expected_final_list_appended, self.test_append_linter.create_final_list())
if __name__ == '__main__':
	unittest.main()
