from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	detail = models.CharField(max_length=400)

	def __str__(self):
		return self.name



