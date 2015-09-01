import os
import re
import tvdb_api
import shutil, errno
from sys import argv
from platform import system

from tvdb_api import tvdb_error
from tvdb_api import tvdb_shownotfound


# CONFIG

# namingFormat = '{{sname}} E{{absolute_number}} - {{episodename}}'
namingFormat = '{{sname}} [{{seasonnumber}}x{{episodenumber}}] - {{episodename}}'
# maxlen

# END CONFIG

# python "C:\Users\Avi\Documents\GitHub\series-renamer\series_renamer.py"
ENC = 'utf-8'
epns = {}
renames = {}

def main(path):
	'''
	Series Renamer commandline program
	'''

	print("What's the series name ? Write it as precise as possible.")
	sname = input()
	getNums(path)
	print("Fetching Series data from TVDB")
	seriesObj = getSeries(sname)

	print()
	ps = 0
	pep = 1
	allgo = done = dont = stop = 0

	strLog = ''

	for i in epns.items():
		dont = done = 0
		print( trimUnicode(i[0]) )
		if len(i[1]) > 1:
			myep,mys = i[1][pep], i[1][ps] if ps>=0 else '0'
		else:
			myep,mys = i[1][0],'0'

		while done == 0:
			print("S " + str(mys) + " , E " + str(myep))
			done = 1
			if allgo == 0:
				print(i[1])
				print("Yes (y) , No (n) , All (a) , Stop (s) , Season change (1) , Episode change (2)")
				x = input().lower()
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
					ps = int(input())
					if ps < 0:
						mys = '0'
					else:
						mys = i[1][int(ps)]
					done = 0
				elif x == '2':
					print('New episode (Give Id) : ', end='')
					pep = int(input())
					myep = i[1][pep]
					done = 0
				else:
					print('Invalid option. Try Again')
					done = 0

		if dont == 0:
			ext = getExtension(i[0])
			title = ''
			if mys == '0':
				epd = seriesObj.search(int(myep), key='absolute_number')
				for epds in epd:
					if epds['absolute_number'] == myep:
						epd = epds
						break
				else:
					print('Episode not found via absolute_number')

				mys = str(epd['seasonnumber'])
				title = epd['episodename']
			else:
				epd = seriesObj[ int(mys) ][ int(myep) ]
				title = epd['episodename']

			newname = makeName(sname, epd) + '.' + ext
			renames[i[0]] = newname
			strLog += '<tr><td>' + i[0] + '</td><td>' + newname + '</td></tr>'

		if stop:
			break

	logfile = path + '\\series_renamer_log.html'
	copyanything( os.path.dirname(os.path.realpath(__file__)) + '\\logs.html', logfile )
	fpt = open(logfile, 'r', encoding=ENC)
	html = fpt.read()
	fpt.close()

	html = html.replace('{{dir}}', os.getcwd() + '\\' + path, 1)
	html = html.replace('{{content}}', strLog, 1)
	fpt = open(logfile, 'w', encoding=ENC)
	fpt.write(html)
	fpt.close()

	print("Log created at " + logfile)
	print("Do you approve renaming ? (y/n)")
	x = input().lower()

	if x == 'y':
		for i in renames.items():
			os.rename(path + '\\' + i[0], path + '\\' + i[1])
		print('Renaming Successful')
		os.remove(logfile)

	return 0


def getNums(path):
	'''
	Scans the path, looks for series files and gets contenders of the episode numbers and season numbers.
	Stores them in epns
	'''

	exts = ['mkv', 'mp4', 'avi', 'flv']

	for i in os.listdir(path):
		if not os.path.isfile(path + '\\' + i):
			continue
		ext = getExtension(i)
		if ext in exts:
			tobj = re.findall("(?i)(.\d+(\s*\-\s*\d+)?)(?=[\. ex\-\]\)\=$])", i) # because of 2 () 2 capturing groups
			if len(tobj):
				epns[i] = tobj


	# fix 264x things
	avoids = []
	for i in epns.items():
		nl = []
		for k in i[1]:
			temp = k[0][0] # so using double reference
			if temp in avoids:
				continue
			nl.append( re.findall("([1-9]\d*(\s*\-\s*[1-9]\d*)?)", k[0])[0][0] )
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


def makeName(sname, eobj):
	'''
	Makes the episode name using the namingFormat
	sname = Name of the series
	eobj = Episode Object containing all other data
	'''

	s = namingFormat
	o = re.findall('\{\{.+?\}\}', s)
	for i in o:
		if i == '{{sname}}':
			s = s.replace(i, fixName(sname), 1)
		else:
			s = s.replace(i, fixName(eobj[ i[2:-2] ]), 1)
	return s


def fixName(s):
	'''
	Removes parts in the string that can't be part of a filename.
	Eg - : in Windows
	'''
	windows = '/\\:*?"<>|'

	if system() == 'Windows':
		for i in windows:
			s = s.replace(i,'')

	return s


# More Functions

def getExtension(fname):
	'''
	Gets extension from the file name. 
	Returns without the dot (.)
	'''
	a = fname.rfind('.')
	return fname[a+1:]


def trimUnicode(s):
	'''
	Trims string s of unicode text
	'''
	return re.sub(r'[^\x00-\x7F]+',' ', s)


def copyanything(src, dst):
	# copy tree from src to dst
	# Taken from Stack Overflow (dont have the link)
	try:
		shutil.copytree(src, dst)
	except OSError as exc: # python >2.5
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		else: raise
	return


# Main

if __name__ == "__main__":
	s = len(argv)
	if len(argv) == 1:
		main('.')
	else:
		if len(argv) == 2:
			main(argv[1])
		else:
			main(argv[1])
