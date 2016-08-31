import os
from setuptools import setup


def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	install_requires = ['tvdb-api'],

	name = "series-renamer",
	version = "1.1.2",
	author = "Avi Aryan",
	author_email = "avi.aryan123@gmail.com",
	description = "Robust TV Series Renamer",
	keywords = "series tv-series tvdb renamer",
	url = "http://github.com/aviaryan/series-renamer",
	packages=['series_renamer'],
	exclude_package_data = {
		'': ['config.json', '__pycache__/*']
	},
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2"
	],
	include_package_data=True, # needed for MANIFEST

	entry_points={
		'console_scripts': [
			'series-renamer = series_renamer.series_renamer:run',
			# 'series-renamer-config = series_renamer.series_renamer:editConfig',
		],
	}
)
