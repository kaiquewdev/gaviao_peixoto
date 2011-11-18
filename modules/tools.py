#!/usr/bin/python
# -*- coding: utf-8 -*-

class Table(object):
	def __init__(self, db='', tablename=''):
		self.table_name = tablename
		self.db = db
		
		db = self.db
		self.tables = {
			'wall': db.wall
		}
	
	def get_contents(self):
		if self.table_name and self.db:
			db = self.db
			
			if self.table_name in self.tables:
				table = self.tables['wall']
			
				count = db(table.id > 0).count()
				selection = db(table.id > 0).select()
			
				if selection and count:
					return {'selection': selection, 'count': count}
			else:
				return False
	
	def get_article(self, id=0):
		db = self.db
		table = self.tables['wall']

		if id > 0 and self.table_name in self.tables:
			query = table.id == id

			return db(query).select().first()
		else:
			return False




