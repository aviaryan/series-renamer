# Series Renamer

[![Version](https://img.shields.io/pypi/v/series-renamer.svg)](https://pypi.python.org/pypi/series-renamer)
[![Downloads](https://img.shields.io/pypi/dw/series-renamer.svg)](https://pypi.python.org/pypi/series-renamer)

Python script that connects to [thetvdb.com](http://thetvdb.com) and renames your TV series in any fashion you want.


### Why another series renamer ?

Other series renaming scripts I tried follow a very error-prone procedure. They scan each filename independently and try to extract all information about the episode from that.
Now my One Piece episodes are named like `opdub283.mp4` and `---one piece episode 691 -u0026 692 english sub full hd.mp4` . How do you expect them to extract any info from this ?

So I decided to make my own *series renamer*. To be able to rename (fix) even badly named files like the above, my script -

* scans the working directory non-recursively
* gets the name of the TV/Anime series the folder has from the user
* gets [TVDB](http://thetvdb.com) information of the TV series the user specified.
* scans through the filenames for potential season numbers / episode numbers. Once you have the series name and the season/episode number accurate, nothing can stop your TV series collection from having a proper name.


## Installing

```bash
pip install series-renamer
```
or download the zip and extract it.

```bash
python setup.py install
```


## Using

* Open **command prompt** aka **terminal** in the directory you want to scan and run the following command.
```
series-renamer
```
* Give the series name. Make sure you write the name as precisely as possible.
* The script will connect to TVDB and then scan the filenames. After that it will give you suggestions on the season numbers/episode numbers of files.
* Choose the appropriate option and move forward. Use option 'a' (automatic) if possible.
* In the end the script will create a log (series-renamer-log.html) in the root of the folder that was currently examined.
* Confirm with (y) and all episodes in the folder will be renamed.


## Features

* Customizable episode renaming format.
* Works even without season information in the filename. It then uses episode_number as the absolute episode_number of the TV Series.
* You can explictly specify season and episode number at runtime.
* Supports multi-episodes separated by hyphen like `Friends [10x17-18].mkv`.
* Subtitle files are automatically renamed.
* More [extra configurations](https://github.com/aviaryan/series-renamer/wiki#configjson) to make sure your tv collection is properly detected and renamed.


## Examples

Some sample logs created by series-renamer can be viewed from [this link](http://aviaryan.github.io/series-renamer/examples/index.html).


## Important

It is recommended you read [some docs](https://github.com/aviaryan/series-renamer/wiki) to be fully comfortable with Series Renamer.


## Requirements

* tvdb-api


## Questions ?

Just create an [issue](https://github.com/aviaryan/series-renamer/issues), I will be glad to be of any help.
