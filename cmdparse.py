#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Command Parse
#---------------------

#Imports
import re

#Internal Imports
from db_config import default_db

#Vairables
default_options=['each','switch']

def start_parsecmd(uinput):
	module_table=default_db('modules')
	cmd=uinput.split('.')
	valid=module_table.find_one(mod_name=cmd[0])
	if valid:
		try:
			input_options = re.findall("'([^']*)'", str(valid['inputs']))
			output_options = re.findall("'([^']*)'", str(valid['outputs']))
			options = list(set(input_options + output_options))

			if cmd[1] in options:
				print '[#]Valid'
			else:
				if cmd[1] == 'help':
					print '[#]Module Name:'+valid['mod_name']
					print '[#]Inputs('+str(valid['inputsint'])+'):'+valid['inputs']
					print '[#]Outputs('+str(valid['outputsint'])+'):'+valid['outputs']
				else:
					print '[!]No Valid Options'

		except:
			print '[#]Module Name:'+valid['mod_name']
			print '[#]Inputs('+str(valid['inputsint'])+'):'+valid['inputs']
			print '[#]Outputs('+str(valid['outputsint'])+'):'+valid['outputs']
	
	else:
		print '[!]Invlaid Command'

#Validate token from the scan script
def validate_token(token):
	module_table=default_db('modules')
	cmd=token.split('.')
	valid=module_table.find_one(mod_name=cmd[0])
	if valid:
		try:
			input_options = re.findall("'([^']*)'", str(valid['inputs']))
			output_options = re.findall("'([^']*)'", str(valid['outputs']))
			options = list(set(input_options + output_options))

			if cmd[1] not in options:
				return 0
				if cmd[2] not in default_options:
					return 0
			
			return 1
		except:
			return 0
	else:
		return 0

	

	