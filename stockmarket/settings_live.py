import redis, os

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
			"hosts": [redis.from_url(os.environ.get("REDIS_URL"))],
		},
		"ROUTING": "stockmarket.routing.channel_routing",
	},
}