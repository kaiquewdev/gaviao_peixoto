#!/usr/bin/python
# -*- coding: utf-8 -*-
import tools

def index():
	table = tools.Table(db, 'wall')
	wall = table.get_contents()
	#Pagination
	limit = 10
	count_articles = 0

	return {'wall': wall, 'limit': limit, 'count_articles': count_articles}

def article():
	args = request.args

	if not args:
		redirect(URL(c='wall', f='index'))
	else:
		

	return {}

def insert():
	pass

def edit():
	pass
