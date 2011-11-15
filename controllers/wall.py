#!/usr/bin/python
# -*- coding: utf-8 -*-
import tools

def index():
	table = tools.Table(db, 'wall')
	wall = table.get_contents()

	return {'wall': wall}

def insert():
	pass

def edit():
	pass
