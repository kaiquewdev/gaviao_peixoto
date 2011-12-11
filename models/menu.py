# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'Gavião Peixoto'
response.subtitle = T('')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
T.force('pt-br')

menu = {
	'off': [
		('Inicio', False, URL('default','index'), []),
		('Mural', False, URL('wall','index'), []),
		('Blog', False, URL('blog','index'), []),
		('Notas', False, URL('notes','index'), []),
		('Contato', False, URL('default','contact'), []),
    ],
    'on': [
    	# Menu for other user, with only.
    ],
    'admin': [
    	('Painel', False, URL('panel', 'index'), []),
    	('Mural', False, URL('wall','index'), []),
		('Blog', False, URL('blog','index'), []),
		('Notas', False, URL('notes','index'), []),
    ],
}

# Normal menu
if auth.has_membership('admin'):
	response.menu = menu['admin']
else:
	response.menu = menu['off']
