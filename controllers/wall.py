#!/usr/bin/python
# -*- coding: utf-8 -*-
import tools

def index():
	args = request.args
	table = tools.Table(db, 'wall')
	limit = 10
	wall = table.get_contents([0, limit])
	numeration = tools.Pagination().get_numeration(wall['count'], limit)

	if args:
		index = int(args[0])
		start = limit*index-limit
		end = limit*index
		wall = table.get_contents([start, end])

	return {'wall': wall, 
			'limit': limit,
			'numeration': numeration, 
			'args': args}

def article():
	args = request.args
	table = tools.Table(db, 'wall')

	if not args:
		redirect(URL(c='wall', f='index'))
	else:
		article = table.get_article(args[0])
		

	return {'article': article}

@auth.requires_membership(role='admin')
def insert():
	form = SQLFORM(Wall, fields=['title', 'cover', 'content'])
	btn_submit = form.element(_type='submit') 

	btn_submit.attributes['_value'] = 'Inserir'
	btn_submit.attributes['_class'] = 'act'

	if form.process().accepted:
		response.flash = 'Novo artigo do mural inserido com sucesso!'
	elif form.errors:
		response.flash = 'Não foi possivel inserir o artigo.'

	return {'form': form}

def edit():
	pass
