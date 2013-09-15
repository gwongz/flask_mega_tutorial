# activates cross-site request forgery prevention
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{ 'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
	{ 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
	{ 'name': 'AOL', 'url': 'http://www.flickr.com/<username>' },
	{ 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
	{ 'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

