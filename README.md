Cranberry
===============================

version number: 0.1.0

author: Daniel Schwabacher

Overview
--------
The short version: Cranberry is a command line solution to easily batch download music from youtube. It sits atop youtube-dl and allows you to upload plaintext files containing song names, which are then downloaded to a directory of your choosing.

The longer one: Cranberry is a complete rewrite of a former project of mine known as autoSong. Like Cranberry, autoSong was a solution to batch download music, however, autoSong had a number of design shortcomings and, as such, is no longer supported in favor of Cranberry. Cranberry is MUCH more user friendly, secure, maintainable and extensible. The ultimate goal of Cranberry is to provide a versatile and customizable music downloading experience through a simple and universal medium (plaintext files).

Installation
--------------------

Cranberry is pip-installable
(the tar distros are here: https://pypi.python.org/pypi/cranberry/)

To install it, run:
```pip3 install cranberry```


The cranberry user guide/workflow:
-------------

###### Cranberry really only needs two things:

1.) A plaintext file (.txt) which contains a list of songs that cranberry should download. The default is songsList.txt located in the user's home directory.

2.) A directory which cranberry will download the songs to. The default is ~/CranberryMusic/

Example:
-------
First, we'll run cranberry with the default settings (no flags):

```cranberry```

This will cause cranberry to look for the file: **~/songsList.txt**. If it is there, cranberry will download all of the songs located in **songsList.txt** to the directory: **~/CranberryMusic/**. **Note: Cranberry will automatically create the download directory if it doesn't exist.**


Cranberry also supports song files with different names in different locations. As an example, we'll specify different song files and directories to download from and to, respectively.

```cranberry -o ~/OtherMusicFiles/ -s ~/other_song_file.txt```

The first flag (-o) is followed by a directory that cranberry will download to. The second flag (-s) is followed by a plaintext file called other_song_file.txt that cranberry will parse songs from.

The built-in cranberry help menu details all the possible flags cranberry accepts, to show it, simply run:

```cranberry -h```

Contributing
---------
TBD

A final disclaimer
-----------
It's no secret that cranberry could potentially be used to download copyrighted work off of youtube (you shouldn't use it for this though). By using this software, you agree that I will not be held responsible for any implications of you downloading or distributing copyrighted work through cranberry.
