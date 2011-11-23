#!/usr/bin/python
# -*- coding: utf-8 -*-
import tools

def index():
	args = request.args
	table = tools.Table(db, 'blog')
	limit = 10
	blog = table.get_contents([0, limit])
	numeration = tools.Pagination().get_numeration(blog['count'], limit)

	if args:
		index = int(args[0])
		start = limit*index-limit
		end = limit*index
		blog = table.get_contents([start, end])

	return {'blog': blog, 
			'limit': limit,
			'numeration': numeration, 
			'args': args}

def post():
	args = request.args
	table = tools.Table(db, 'blog')

	if not args:
		redirect(URL(c='blog', f='index'))
	else:
		post = table.get_article(args[0])
		

	return {'post': post}
