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
	
	def get_contents(self, limit=[]):
		if self.table_name and self.db:
			db = self.db
			
			if self.table_name in self.tables:
				table = self.tables['wall']
			
				count = db(table.id > 0).count()
				if not limit:
					selection = db(table.id > 0).select(orderby=~table.created_on)
				elif limit and len(limit) == 2:
					selection = db(table.id > 0).select(orderby=~table.created_on, limitby=(limit[0], limit[1]))
				else:
					return False

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

class Pagination(object):
	def get_numeration(self, total_articles=0, limit_articles=0):
		'''
		>>> Pagination().get_numeration(20, 10)
		2
		>>> Pagination().get_numeration(20, 0)
		False
		>>> Pagination().get_numeration(10, 20)
		1
		>>> Pagination().get_numeration(27, 10)
		3
		'''
		total = total_articles
		limit = limit_articles

		if total > 0 and limit > 0:
			if total/limit == 0:
				return (total/limit)+1
			elif total%limit > 0:
				return (total/limit)+1
			else:
				return (total/limit)
		else:
			return False
	def skeleton():
		pass


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
	_test()