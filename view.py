#!/usr/bin/env python

# -------------------------------------------------------
# Talwar version 0.1 
# Web application vulnerability scanner
# Talwar View
# -------------------------------------------------------

#Imports
import sys
import dataset



def database_view(db_name):
	db = dataset.connect('sqlite:///Databases/'+db_name+'.db')
	
	heartbleed = db['heartbleed_test']
	
	return heartbleed


