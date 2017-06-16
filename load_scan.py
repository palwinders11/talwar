#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Load Scan v.1
#---------------------

#Imports
import sys

# Internal Imports
from parser import start_parser

def config_load(file_name):
	try:
		with open(file_name+'.tl', 'r') as content:
			output=content.read()
		pipeline= output.replace('\n', ' ').replace('\r', '')
		print '[!]Your Pipeline:>' + pipeline
		is_valid,tokens=start_parser(pipeline)
		return is_valid,tokens
	except:
		print '[!]Error: Unable to find the file'
		print '[#]Make sure to put your scan in \'Scans\' folder'
		return False,0


