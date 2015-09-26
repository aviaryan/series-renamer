---
layout: default
title: Series Renamer
---

<a name="intro"></a>
<h2 id="intro">Introduction</h2>
Series Renamer is a robust TV series renaming command-line application written in Python. It uses the TVDB API to fetch extra data about episodes and uses that to rename the files.

To start using it, you first need to install the script. For that, please follow these steps -

* [Download zip](https://github.com/aviaryan/series-renamer/archive/master.zip) and extract it.
* From the extracted folder, run

```bash
# requires tvdb-api
python setup.py install
```


<a name="using"></a>
<h2 id="using">Using</h2>

* Open command prompt aka terminal in the directory you want to scan and run the following command.

```
series-renamer
```

* Give the series name. Make sure you write the name as precisely as possible.
* The script will connect to TVDB and then scan the filenames. After that it will give you suggestions on the season numbers/episode numbers of files.
* Choose the appropriate option and move forward.
* In the end the script will create a log (series-renamer-log.html) in the root of the folder that was currently examined.
* Confirm with (y) and all episodes in the folder will be renamed.


<a name="numbers"></a>
<h2 id="numbers">Season and Episode Numbers</h2>
The Season and Episode numbers are the base of Series Renamer. It scans through the file names and extracts the numbers which it thinks can be season number or episode number. 
When in the user confirmation phase, it displays the detected season and episode number and gives option to the user to change it if need. Multi-episodes are supported as long as they are of the format *StartEp*-*EndEp* (example, *Friends [10x23-24] - The Last One.mkv*).

For changing season number, it's 1 whereas for episode number, it's 2.

When changing season number, you can put these types of values.

* `#N` - Explictly speciify the season number `N`. This season number value will be used for all future episodes and so it is highly recommend to use this option only when the folder being scanned has episodes from a single season.
* `N` where `N` is a positive/zero number - Changes the season number to the `N`th item in array i.e. changes season index to `N`. This index will be remembered for future episodes. Please keep in mind that here array starts from 0.
* `-1` - Sets the season to 0 meaning no season. In this case, episode is looked through its absolute number of episode.

When changing episode number, you can put these types of values.

* `N` where `N` is a positive/zero number - Changes the episode number to the `N`th item in array i.e. changes episode index to `N`. This index will be remembered for future episodes. Here also index starts from 0.

In case of season and episode numbers, any custom change made by the user (by pressing 1 or 2) is remembered by the script and used for future episodes. But when the number of 
array items is equal to 1, then season number is set to `#N` or 0 and episode number is set to *array[0]*.


<a name="config"></a>
<h2 id="config">Configuration</h2>
Series Renamer can be configured by calling `series-renamer config`. This will open the config.json file in the default text editor. There are currently 2 settings in series-renamer.

**namingFormat**

The format to rename episodes. variables are enclosed in \{\{..\}\}. Common variables are - 

* episodename
* episodenumber
* seasonnumber
* absolute\_number - The absolute number of an episode. Eg for Friends S02E01, absolute number = 25.
* sname - The series name specified by user at the beginning.

**replaces**

Temporary find-and-replace script does when scanning file names for numbers. This feature can be used to rule out unwanted potential numbers and even fix detected numbers.

For example, my [One Piece episodes](examples/one_piece_mixed.html) had names like *one piece 657 -u0026 658.mp4*. Now as series-renamer only detects `N1 - N2` as multi-episode, so I replaced '-u0026' with '-'.
Also some episodes were like *one piece 456 & 457 blah blah YouTube.mp4*. So I also replaced '&' with '-'.
Therefore replaces became - 

```json
"replaces": {
    "&": "-",
    "-u0026": "-"
}
```

NOTE - To prevent some number from being detected by series-renamer, preceed it by ~ (tilde). Example my beyblade episode was like *Beyblade 145 03.mp4*, where 145 was some number that gave nothing useful. So I replaced 'Beyblade ' with '~'.

```json
"replaces": {
    "Beyblade ": "~"
}
```


<a name="examples"></a>
<h2 id="examples">Examples</h2>
Some sample logs created by series-renamer can be viewed from [examples/index.html](examples/index.html). To rename such badly named episodes, the 'replaces' config came very useful. 