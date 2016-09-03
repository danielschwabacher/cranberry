import re
""" Sensor objects are used to manipulate the raw data in the song file into 
a format usable by Cranberry. While it may seem like Sensor objects don't do much now, I plan
to implement many features into the class, that is why it is its own class.
These objects are to be used as helpers for parser objects and not own their own 

---More info about sensors: sensors will eventually be the backbone of Cranberry's 
versatile architecture. They will allow users to specify a certain parse pattern
to provide a quick and easy way to batch download music. A design goal of sensors is to keep them modular and 
extensible so users can implement their own sensors. The default sensor is 
default, which removes numbers from the raw song_strings. 

----A use case for sensors: to be written later
"""
class Sensor():
    """ Yes, this is a sensor because it specifically modifies the raw data in the song file
    in a certain way. This is the most rudimentary sensor possible, as it only removes 
    numbers from the raw strings. As the default sensor, it provides reliable performance on 
    most of the textual patterns found in the plaintext songfiles. You wouldn't want to use this 
    sensor if you were downloading songs that contained numbers. """
    def default(self, src):
        revised_list = []
        for line in src:
            edit = re.sub(r'[^.a-zA-Z" "]', "", line)
            revised_list.append(edit)
        return revised_list


