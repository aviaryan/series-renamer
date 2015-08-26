import os
import re
import tvdb_api
import series_renamer_gui
from sys import argv

from tvdb_api import tvdb_error
from tvdb_api import tvdb_shownotfound


epns = {}
namingFormat = '{name}.s{season}e{episode}.{title}'


def main(path):
	'''
	Series Renamer commandline program
	'''

	print("What's the series name ?")
	sname = input()
	getNums(path)
	seriesObj = getSeries(sname)

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
			myep,mys = i[1][0],'0'
		print("S " + str(mys) + " , E " + str(myep))

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
					ps = input()
					mys = i[1][ps]
				elif x == '2':
					print('New episode (Give Id) : ', end='')
					pep = input()
					myep = i[1][pep]
				else:
					print('Invalid option. Try Again')
					done = 0

		if dont == 0:
			ext = getExtension(i[0])
			newname = namingFormat.replace('{name}', sname).replace('{season}', mys).replace('{episode}', myep).replace('{title}', sname) + '.' + ext
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
		ext = getExtension(i)
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
	Throws exception if something goes wrong
	'''

	x = 0
	try:
		t = tvdb_api.Tvdb()
		x = t[sname]
	except tvdb_error:
		print("There was an error connecting the TVDB API\n")
	except tvdb_shownotfound:
		print("Show Not Found on TVDB\n")
	except Exception:
		print("There was an error. Tvdb API")
	return x


# More Functions

def getExtension(fname):
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