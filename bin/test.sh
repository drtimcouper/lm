#!/bin/sh

nosetests --with-coverage --cover-erase --cover-html --cover-html-dir=cover --cover-package=lmsuite
