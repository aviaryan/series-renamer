import os
import re
import tvdb_api
import series_renamer_gui
from sys import argv


epns = {}
namingFormat = '{name}.s{season}e{episode}.{title}'


def main(path):
	'''
	Series Renamer commandline program
	'''

	print("What's the series name ?")
	sname = input()
	getNums(path)

	print()
	ps = 0
	pep = 1
	allgo = done = dont = stop = 0

	strLog = ''

	for i in epns.items():
		dont = done = 0
		print(i[0])
		if len(i[1]) > 1:
			myep,mys = i[1][pep],i[1][ps]
		else:
			myep,mys = i[1][0],0
		print("Season - " + mys + "\nEpisode - " + myep)

		while done == 0:
			done = 1
			if allgo == 0:
				print(i[1])
				print("Yes (y) , No (n) , All (a) , Stop (s) , Season change (1) , Episode change (2)")
				x = input()
				if x == 'y': 
					continue
				elif x == 'n':
					dont = 1
				elif x == 'a': 
					allgo = 1
				elif x == 's': 
					dont = stop = 1
					break
				elif x == '1':
					print("New season (Give Id) : ", end='')
					mys = ps = int(input())
				elif x == '2':
					print('New episode (Give Id) : ', end='')
					myep = pep = int(input())
				else:
					print('Invalid option. Try Again')
					done = 0

		if dont == 0:
			newname = namingFormat.replace('{name}', sname).replace('{season}', mys).replace('{episode}', myep)
			strLog += i[0] + " -> " + newname + '\n'
		if stop:
			break

	print(strLog)
	return 0


def getNums(path):
	'''
	Scans the path, looks for series files and gets the episode numbers and season numbers
	'''

	exts = ['mkv', 'mp4', 'avi', 'flv']

	for i in os.listdir(path):
		if not os.path.isfile(path + '\\' + i):
			continue
		ext = getExtenstion(i)
		if ext in exts:
			tobj = re.findall("(?i).\d+(?=[\. \-e$])", i)
			if len(tobj):
				epns[i] = tobj


	# fix 264x things
	avoids = ['x']
	for i in epns.items():
		nl = []
		for k in i[1]:
			temp = k[0]
			if temp in avoids:
				continue
			nl.append( re.findall("\d+", k)[0] )
		epns[i[0]] = nl


	# for k in epns.items():
	# 	print(k[1])
	# 	#print(" : " + epns[k])
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