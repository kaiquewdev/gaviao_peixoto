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
	table = tools.Table(db, 'wall')

	if not args:
		redirect(URL(c='wall', f='index'))
	else:
		article = table.get_article(args[0])
		

	return {'article': article}

def insert():
	pass

def edit():
	pass
