import os
import re
import tvdb_api
import series_renamer_gui
from sys import argv


epns = {}
seasons = {}
sname = '{name}.s{season}e{episode}.{title}'


def main(path):
	'''
	Series Renamer commandline program
	'''

	print("What's the series name ?")
	sname = input()
	getEpisodeNos(path)

	return 0

def getEpisodeNos(path):
	'''
	Scans the path, looks for series files and gets the episode numbers and seasons
	'''

	exts = ['mkv', 'mp4', 'avi', 'flv']

	for i in os.listdir(path):
		if not os.path.isfile(path + '\\' + i):
			continue
		ext = getExtenstion(i)
		if ext in exts:
			tobj = re.findall("(?i)\Ws[a-z]{0,5}\W*\d+", i)
			if len(tobj):
				seasons[i] = tobj
			tobj = re.findall(".\d+(?=[\. \-])", i)
			if len(tobj):
				epns[i] = tobj

	# Totally fix the seasons
	for i in seasons.items():
		if len(i[1]) != 1:
			del seasons[i[0]]
		else:
			seasons[i[0]] = re.findall("\d+", i[1][0])[0]


	# Decide for Episodes
	avoids = ['x']
	for i in epns.items():
		nl = []
		for k in i[1]:
			temp = k[0]
			if temp in avoids:
				continue
			nl.append(k)
		epns[i[0]] = nl
	

	for k in epns.items():
		print(k[1])

	for k in seasons.items():
		print(k)
		#print(" : " + epns[k])
	return


def make():
	'''
	'''
	return

def getSeries(sname):
	'''
	Gets Series data using the TVDB API
	'''
	t = tvdb_api.Tvdb()
	return t[sname]
	# TODO use exception


# More Functions

def getExtenstion(fname):
	''' gets extension from the file name '''
	a = fname.rfind('.')
	return fname[a+1:]


# Main

if __name__ == "__main__":
	s = len(argv)
	if s > 1:
		main(argv[1])
	else:
		series_renamer_gui.main()