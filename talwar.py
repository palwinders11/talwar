#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Main Start
#---------------------

#Import
import os
import socket
from urlparse import urlparse

#Interal Imports
from importmodules import start_importmodules
from cmdparse import start_parsecmd
from parser import start_parser
from execute import execute_pipeline
from view import database_view
from load_scan import config_load

#Desgin Test
Btextstart = "\033[1m"
Btextend = "\033[0;0m"

#Default Domain
global target,start_valid,tokens
target=0
start_valid=False
tokens = 0


#start scan
def startscan():
	if start_valid:
		print '[#]Starting scans..'
		if tokens != 0:
			execute_pipeline(target,tokens)
		else:
			print '[!]Unable to get scan config'
	else:
		print '[!]Scan Not confgiured. Use \'config\' to configure scan.'


#cleart screen
def clear():
	try:
		os.system('clear') 
	except:
		os.system('cls')

# Confgiure Scan
def config_scan():
	global start_valid,tokens
	if target != 0:
		pipeline=raw_input(Btextstart+'pipeline:>'+Btextend)
		is_valid,tokens=start_parser(pipeline)
		if is_valid:
			start_valid=True
		else:
			start_valid=False
	else:
		print '[!]Target not set'
		print '[!]Use \'target\' to set target'

#Validate Domain
def validate_target(target):
	if urlparse(target).netloc != '':
		target=urlparse(target).netloc

	try:
		if socket.gethostbyname(target):
			return True
	except socket.error:
		return False


#Get Domain
def gettarget():
	try:
		global target
		target=raw_input(Btextstart+'target:>'+Btextend)
		if validate_target(target):
			print '[#]Target Accuried'
		else:
			print '[!]Invalid Target'
			print '[!]Might be a connectivity issue'
	except:
		print '[!]Invalid Target'

# Update Modules
def updatemodules():
	try:
		print '[#]Updating Modules...'
		start_importmodules()
		return 1
	except:
		return 0

# Update Modules starts
def updatemod():
	if updatemodules():
		print '[#]Update Completed'
		listner()
	else:
		print '[#]Unable to Update'
    	skip=raw_input('Want to skip update?[Y/n]')
    	if skip == 'Y' or skip == 'y':
    		listner()
    	elif skip == 'N' or skip == 'n':
    		exit()
        else:
        	print '[#]Invalid input'
        	listner()

# Help function
def help():
	print 'Talwar Version 0.2'
	print 'By Gurjant Singh'

def owner():
	print 'He is our god.'

# Exit Program
def exit():
	os._exit(1)

#View target database results
def view():
	heartbleed=database_view(target)
	
	for domain_name in heartbleed:
	    print domain_name

#Load Config Scan
def load_scan():
	global start_valid,tokens
	if target != 0:
		 file_name=raw_input(Btextstart+'file_name:>'+Btextend)
		 is_valid,tokens=config_load(file_name)
		 if is_valid:
		 	start_valid=True
		 else:
		 	start_valid=False
	else:
		print '[!]Target not set'
		print '[!]Use \'target\' to set target'


# Default Commands
command = { 'help' : help,
           'exit' : exit,
           'view' : view,
           'updatemod' : updatemod,
           'target' : gettarget,
           'start'  : startscan,
           'config' : config_scan,
           'clear' : clear,
           'gurjant' : owner,
           'loadscan' : load_scan
}

# Start Listing for commands
def listner():
	while True:
		uinput=raw_input(Btextstart+'talwar#'+Btextend)
		try:
			command[uinput]()
		except: 
			start_parsecmd(uinput)

#start program
def main():
   listner()

main()