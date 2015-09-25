import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "series-renamer",
    version = "0.1",
    author = "Avi Aryan",
    author_email = "avi.aryan123@gmail.com",
    description = "Renames your tv series",
    license = "Apache",
    keywords = "series tv-series tvdb renamer",
    url = "http://github.com/aviaryan/series-renamer",
    packages=['series_renamer'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Topic :: Utilities",
        "License :: Apache License v2.0",
    ],
    include_package_data=True, # needed for MANIFEST

    entry_points={
        'console_scripts': [
            'series-renamer = series_renamer.series_renamer:run',
        ],
    }
)