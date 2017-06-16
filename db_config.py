#!/usr/bin/env python

#---------------------
# Talwar v 0.2
# Import Modules
#---------------------

#Import Internal files
import dataset


#Default Database for Talwar
def default_db(table_name):
	db = dataset.connect('sqlite:///Databases/talwar.db')
	table = db[table_name]
	return table


def connect_db(db_name,table_name):	
	db = dataset.connect('sqlite:///Databases/'+db_name+'.db')
	table = db[table_name]
	return table
