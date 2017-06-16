#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Execution Program v.1
#---------------------

#Imports
import thread
import sys

#Internal Imports
from db_config import default_db,connect_db

#Default tokens
default_tokens=['start','end','then']


#sys.path.append('Modules/') 
#					mod=__import__(module[0])
#					if module[1] == 'domain_name':
#						print 'Module included'
#					else:
#						print '[!] Input for ' + module + ' moudle not present'

#Start moudle
def start_module(mod_name,input,db_name):
	sys.path.append('Modules/') 
	mod=__import__(mod_name)
	try:
		print "[*]Starting Module " + mod_name + " for " + input
		mod.start_talwar(db_name,input)
	except:
		print '[!]Some Problem with ' + mod_name 
		print '[!]Check if the module is properly configured.'



#Build Scan
def build_scan(target,tokens):
	if tokens[0] == 'target':
		if tokens[1] == '->':
			if len(tokens) > 3:
				print "other parameter"
			else:
				module=tokens[2].split('.')
				mod_name=module[0]
				
				start_module(mod_name,target,target)
		else:
			print '[!] You might miss the \'->\' in config flow'
	else:
		module_input=tokens[0].split('.')
		try:
			module_table=connect_db(target,module_input[0])
			if tokens[1] == '->':
				if len(tokens) > 3:
					print "other parameter"
				else:
					module_output=tokens[2].split('.')
					try:
						if module_input[2] == 'each':
							each=True
						else:
							print '[!]Error: Unknown option ' + module_input[2]
							each = False
					except:
						each = False
					if each:
						for each in module_table:
							start_module(module_output[0],each[module_input[1]],target)
					else:
						for each in module_table.find(id=1):
							start_module(module_output[0],each[module_input[1]],target)
				
			else:
				print '[!] You might miss the \'->\' in config flow'

		except Exception as e:
			print '[!] Unable to find the ' + modulep[0] + ' module results in database'
			print e



#Start Execute
def execute_pipeline(target,tokens):
	start_index=0
	for index,token in enumerate(tokens):
		if token in default_tokens:
			if start_index == 0:
				start_index=index+1
			else:
				build_scan(target,tokens[start_index:index])
				start_index=index+1



		#if token !='start' or token != 'end':
	#		if token not in default_tokens:
	#			if start_index == 0:
	#				start_index=index
	#			else:
	#				end_index=index
	#				build_scan(tokens[start_index:(end_index+1)])
	#				start_index=0
	#				end_index=0



	#for index,token in enumerate(tokens):
	#	if token == 'target' and tokens[index+1] == '->':
	#		module=tokens[index + 2]
	#		thread1=thread.start_new_thread(input_target, (target,module))
	#		thread1.start()
	#	else:
	#		print '[!]Error: Target should only be a input.'

#Starting modules
def input_target(target,module):
		print "hello"
		mod_name=module.split('.')[0]
		sys.path.append('Modules/')
		mod=__import__(mod_name)
		mod.start_talwar(target)