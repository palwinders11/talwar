#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Parser v.1
#---------------------

#Internal Imports
from cmdparse import validate_token

#Default Tokens
default_tokens= ['start','end','also','then','->','target']

#Variable
global error_count
error_count=0

#Starting Parser
def start_parser(pipeline):
	global error_count
	error_count=0
	tokens=pipeline.split()
	if tokens.count('start') != 1 or tokens.count('end') != 1:
		print '[!]start and end keywords should only be used onces.'
		return False,0
	else:
		if tokens[0] == 'start' and tokens[len(tokens)-1] == 'end':
			for token in tokens:
					validate(token)
			if error_count !=0:
				return False,0
			else: 
				return True,tokens
		else:
			print '[!] Pipeline should start with end with \'start\' and \'end\' keywords respectivily'
			return False,0

#Validate each token 
def validate(token):
	global error_count
	if token not in default_tokens:
		if token == 'target.each':
			print '[!]Error: \'target.each\' target don\'t have each option'
			error_count +=1
		elif validate_token(token):
			print 'valid'
		else:
			print '[!]Error:'+token+' invalid'
			error_count +=1
		