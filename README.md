# Series Renamer (beta)

Python script that connects to [thetvdb.com](http://thetvdb.com) and renames your TV series in any fashion you want.


### Why another series renamer ?

Other series renaming scripts I tried follow a very error-prone procedure. They scan each filename independently and try to extract all information about the episode from that.
Now my One Piece episodes are named like `opdub283.mp4` . How do you expect them to extract any info from this ?

So I decided to make my own *series renamer*. To be able to rename (fix) even badly named files like the above, my script -

* scans the working directory non-recursively
* gets the name of the TV/Anime series the folder has from the user
* gets [TVDB](http://thetvdb.com) information of the TV series the user specified.
* scans through the filenames for potential season numbers / episode numbers. Once you have the series name and the season/episode number accurate, nothing can stop your TV series collection from having a proper name.


## Installing

Download the zip.
```bash
python setup.py install
# python3 setup.py install
# for ubuntu/debian users
```


## Using

* Open **command prompt** aka **terminal** in the directory you want to scan and run the following command.
```
series-renamer
```
* Give the series name. Make sure you write the name as precisely as possible.
* The script will connect to TVDB and then scan the filenames. After that it will give you suggestions on the season numbers/episode numbers of files.
* Choose the appropriate option and move forward.
* In the end the script will create a log (series-renamer-log.html) in the root of the folder that was currently examined.
* Confirm with (y) and all episodes in the folder will be renamed.


## Features

* Customizable episode renaming format.
* Works even without season information in the filename. It then uses episode_number as the absolute episode_number of the TV Series.
* You can explictly specify season and episode number at runtime.
* More [features](http://aviaryan.github.io/series-renamer/index.html#config) to make sure your tv collection is properly detected and renamed.


## Examples

Some sample logs created by series-renamer can be found in the [examples](https://github.com/aviaryan/series-renamer/tree/gh-pages/examples) folder. You can view them online from [this link](http://aviaryan.github.io/series-renamer/examples/index.html)


## Important

It is recommended you read [some docs](http://aviaryan.github.io/series-renamer/index.html#numbers) to be fully comfortable with Series Renamer.


## Requirements

* tvdb-api
* Python 3

