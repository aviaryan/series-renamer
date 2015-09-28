import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    install_requires = ['tvdb-api'],

    name = "series-renamer",
    version = "0.2",
    author = "Avi Aryan",
    author_email = "avi.aryan123@gmail.com",
    description = "Robust TV Series Renamer",
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
            # 'series-renamer-config = series_renamer.series_renamer:editConfig',
        ],
    }
)