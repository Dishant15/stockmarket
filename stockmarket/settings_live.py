# import redis, os
ALLOWED_HOSTS = [ 'localhost:8000', 'stockmarket15.herokuapp.com' ]


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'dammhh2kmloj95',
		'USER': 'dsaxlmjvftbtfb',
		'PASSWORD': '2a70d3b96228c3d9e42821e21f9b9b1237ddfe8e25e66903807c29516ce605e6',
		'HOST' : 'ec2-54-243-38-139.compute-1.amazonaws.com',
		'PORT' : '5432',
	},
}

# Channel settings
CHANNEL_LAYERS = {
	"default": {
		"BACKEND": "asgi_redis.RedisChannelLayer",
		"CONFIG": {
			"hosts": ['redis://h:p72f1b7179844f7b4176f39c923bd37660d6498ce9657e6d6d0d809c01ed4f96b@ec2-34-198-196-38.compute-1.amazonaws.com:41759'],
		},
		"ROUTING": "stockmarket.routing.channel_routing",
	},
}