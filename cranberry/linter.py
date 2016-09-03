from cranberry import sensor
import re

class Linter():
    """ The Linter class is used to parse the source_file to create a 
    usable representation of the data it contains. 
    FYI: while this class is called linter, it is not such 
    in a conventional sense. It is named that to avoid conflicts 
    with argparse, it really is more of a parser. """
    def __init__(self, source_file):
        self.source_file = source_file
    
    # return a python list data structure containing a list of song names
    def create_songs_list(self, src):
        song_list= []
        with open(src, 'r') as song_file:
            for line in song_file:
                song_list.append(line)
        return song_list

    # Automatically adds the '+' between words to ensure compatibility with youtube-dl
    def add_query_compatibility(self, src):
        compatible_list = []
        for line in src:
            appendable = line.replace(" ", "+")
            compatible_list.append(appendable)
        return compatible_list

    # run the specified sensor
    def song_sense(self, src):
        using_sensor = sensor.Sensor()
        return using_sensor.default(src)

    def create_final_list(self, src):
        list_1 = self.create_songs_list(src)
        list_2 = self.song_sense(list_1, )
        final_list = self.add_query_compatibility(list_2)
        return final_list
