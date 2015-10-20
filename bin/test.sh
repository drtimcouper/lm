#!/bin/sh

nosetests -v --with-coverage --cover-erase --cover-html --cover-html-dir=cover --cover-package=lmsuite
