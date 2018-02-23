Cranberry
===============================
[![PyPI version](https://badge.fury.io/py/cranberry.svg)	](https://pypi.python.org/pypi/cranberry/1.0.0)[![dls](https://img.shields.io/github/downloads/danielschwabacher/cranberry/total.svg)	](
http://github.com/danielschwabacher/cranberry)[![release](https://img.shields.io/github/release/danielschwabacher/cranberry/all.svg)	](https://github.com/danielschwabacher/cranberry)

Cranberry is a flexible solution for batch downloading music. It sits atop [youtube-dl](https://github.com/rg3/youtube-dl) and accepts plaintext files specifying music to download. Cranberry is user friendly and highly extensible. The ultimate goal of this project is to provide a versatile and customizable music downloading experience through a simple and universal medium (plaintext files).

Overview
--------
Cranberry parses plaintexts files for music. After it finds song names in these files, it searches youtube (or another video service) for the matching video. Cranberry then uploads the relevant URLs to youtube-dl, which downloads and converts the video to an MP3. 


Installation
--------------------
Cranberry is distributed via a PyPi. The current PyPi index, along with the tar distros can be found here: https://pypi.python.org/pypi/cranberry/1.0.0 

The easier way to install cranberry is with pip. Simply run the folllowing:
```pip install cranberry```


Basic Usage Guide
-------------
Cranberry is a command line interface (CLI) meaning that, once installed, the program can be invoked via a command line by running the command: ```cranberry```.  This will print a help menu and then exit. 

Cranberry Sessions
-------
 A cranberry session requires two arguments to run. 
 
 1.) A source file, denoted by ```-s``` 
  * This is a plaintext file containing a list of songs to download. 
  * If left unspecified, cranberry will look for songs in the file ```~/songsList.txt```
  * The format of this song file is detailed in the section **Song Files**.
  
 2.) An output directory, denoted by ```-o```
 * This is the directory which cranberry will download the MP3s to
 * If left unspecified, cranberry will download the songs to ```~/CranberryMusic```

### Basic usage 
The following example shows how to download music contained in the file **songs.txt** to the directory **~/music**:
* ```cranberry -s songs.txt -o ~/music```


### More options

##### Append "audio" <a id="append"></a>

Sometimes, especially on Youtube, appending the text "audio" to your search queries results in more accurate matches. Cranberry has a handy flag to automatically append this to your searches, to run cranberry in append mode, use the ```-a``` flag
* ```cranberry -a -s songs.txt -o ~/music```

##### Delay requests <a id="delay"></a>
Youtube may throttle or deny your requests if you spam the site with a lot of requests in a short period of time. Cranberry has a flag (```-r NUM_SECONDS``` ) to add a delay, in seconds, to your requests to mitigate this issue.
* ```cranberry -r 2 -s songs.txt -o ~/music```
* This will run cranberry with a 2 second delay between Youtube requests
* Note that higher values may significantly increase  the time cranberry takes to finish

For more rigorous pattern matching and parsing options, see the section entitled **Sensors**

Song Files
----------
Song files are simply .txt files which may contain individual song names, artists, albums, etc. In cranberry's default mode, each line, delimited by the newline character (return), will be searched on Youtube. The first result of each search will be downloaded as a MP3 file. 

For example, suppose you want to download all of Beethoven's first 5 symphonies. To do this, you'd construct a file, 
**Beethoven_songs.txt**, containing: 

**Beethoven_songs.txt**

| Beethoven Symphony No. 1 |

| Beethoven Symphony No. 2 |

| Beethoven Symphony No. 3 |

| Beethoven Symphony No. 4 |

| Beethoven Symphony No. 5 |


Cranberry works best when your song file contains specific enough queries such that the first Youtube search result is what you're looking for. Again, using the [append](#append) flag can help ensure you download the expected content. 

Sensors
---------
Sensors are the backbone of cranberry. They specify parsing and search patterns. Cranberry downloads the first result returned by Youtube's search. Using the right sensor can ensure the first Youtube search result is the most relevant one to your use case. 

#### Default sensor
The default sensor simply removes numbers and colons from each search query. For example, if your song file contains timestamps along with song names, only the song names will be uploaded to the Youtube search. The following table may help illustrate:

|Actual Song File Text  | Uploaded to Youtube |
|-----------------------|---------------------|
|  10:15 SONG_NAME      |       SONG_NAME     |
|  Beethoven No. 1      |       Beethoven No. |


The default sensor is not a good choice for downloading songs which contain numbers (like the symphonies), as the numbers won't be reflected in the Youtube search. 

#### Other sensors
Currently, cranberry just has the one default sensor. I'll be adding more in the future to handle more use cases. 

#### Custom sensors
Sensors can, technically, be anything, from simply regex pattern matches to artificially intelligent systems which best pick out which items to search. Cranberry will support custom, user-defined sensors. The architecture for this system is currently a work in progress. 


Troubleshooting
-------------------
The most likely problem you'll experience with cranberry is Youtube blocking your requests for long song files. To help remedy this, specify a reasonable number of seconds between requests using the [delay](#delay)  flag. 

Contributing
---------
Contributions are very welcome. Feel free to fork this repository and add some features. 

A final disclaimer
-----------
There is a lot of non-copyrighted, free, and good music on Youtube. Cranberry was developed to make downloading this music less tedious. Without cranberry, the best option is often to upload individual Youtube URLs to a music downloading service (for example, http://youtubemp3.to/). This takes a long time. 

You shouldn't use cranberry to download copyrighted works. And, by using this software, you agree that I will not be held responsible for any implications of you downloading or distributing copyrighted work through cranberry.
