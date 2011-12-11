#!/usr/bin/python
# -*- coding: utf-8 -*-
import tools as t

@auth.requires_membership(role='admin')
def index():
	articles = t.Table(db, 'wall').get_contents()
	posts = t.Table(db, 'blog').get_contents()
	
	return {'articles': articles, 'posts': posts}
