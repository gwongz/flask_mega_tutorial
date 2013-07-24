"""Settings required for Flask-WTF extension"""

CSRF_ENABLED = True
SECRET_KEY = 'sld;kfja;dlkfja'

# define list of OpenID providers

OPENID_PROVIDERS = [
	{ 'name': 'Google', 'url': 'https://www.google.com/accounts/08/id' },
	{ 'name': 'Yahoo', 'url': 'http://me.yahoo.com' },
	{ 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
	{ 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
	]