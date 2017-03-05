from __future__ import unicode_literals

from django.db import models

class Stocks(models.Model):
	name 		= models.CharField( max_length = 10 )
	timestamp 	= models.DateTimeField( auto_now_add = True )

	class Meta:
		verbose_name = "Stock"
		verbose_name_plural = "Stocks"

	def __unicode__(self):
		return self.name
