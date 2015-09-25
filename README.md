# Series Renamer

Python script that connects to [tvdb.com](http://tvdb.com) and renames your TV series in any fashion you want.


### Why another series renamer ?

Other series renaming scripts I tried follow a very error-prone procedure. They scan each filename independently and try to extract all information about the episode from that.
Now my One Piece episodes are named like `opdub283.mp4` . How do you expect them to extract any info from this ?

So I decided to make my own *series renamer*. To be able to rename (fix) even badly named files like the above, my script -

* accepts folder to scan as the parameter
* gets the name of the TV/Anime series the folder contains from the user
* scans through the filenames for potential season numbers / episode numbers. Once you have the Series name and the Season/Episode accurate, nothing can stop your tv series collection from having a proper name.


## Installing

```
python setup.py install
```


## Using

* Run the script optionally passing the directory to scan as the parameter
```bash
python series-renamer.py <path-to-folder>
# or
# python series-renamer.py
```
* Give the series name. Make sure you write the name as precisely as possible.
* The script will connect to TVDB and then scan the filenames. After that it will give you suggestions on the season numbers/episode numbers of files.
* Choose the appropriate option and move forward.
* In the end the script will create a log (series-renamer-log.html) in the root of the folder that was currently examined.
* Confirm with (y) and all episodes in the folder will be renamed.