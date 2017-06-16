#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Import Modules
#---------------------

#Import Modules
import glob
import sys

#Internal Imports
from db_config import default_db

#Default Variable


# Start Import Modules
def start_importmodules():
	module_table=default_db('modules')
	try:
		for module in glob.iglob('./Modules/*.py'):
			try:
				mod_name=module.split('/')[2].split('.')[0]
				sys.path.append('Modules/')
				mod=__import__(mod_name)
				try:
					config=mod.config_talwar()
					module_table.insert({'mod_name': module.split('/')[2].split('.')[0], 'inputsint': len(config['inputs']),'outputsint': len(config['outputs']),'inputs': str(list(config['inputs'])),'outputs': str(list(config['outputs']))})
					print '[#]'+mod_name+' imported!'
				except:
					print '[!]Unable to Configure the module'
			except:
				print '[!]Unable to find the default functions for Talwar imports in ' + module.split('/')[2].split('.')[0] + ' module.'
	except:
		print '[!]Some problem with importing modules'
	        