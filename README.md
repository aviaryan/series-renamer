# Series Renamer

Python script that connects to [tvdb.com](http://tvdb.com) and renames your TV series in any fashion you want.


#### Why another series renamer ?

Other series renaming scripts I tried follow a very error-prone procedure. They scan each filename independently and try to extract all information about the episode from that.
Now my One Piece episodes are named like `opdub283.mp4` . How do you expect them to extract any info from this ?

So I decided to make my own *series renamer*. To be able to rename (fix) even badly named files like the above, my script -

* gets the TV series name from the user
* scans through the filenames for potential season numbers / episode numbers. Once you have the Series name and the Season/Episode accurate, nothing can stop your tv series collection from having a proper name.


## Installing

```
easy_install something
```


## Using

