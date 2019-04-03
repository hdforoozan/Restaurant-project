from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Food(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	image = models.ImageField(upload_to='images/',null=True)
	pub_date = models.DateTimeField(auto_now=False)
	price = models.PositiveIntegerField()
	detail = models.CharField(max_length=400)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('food-detail', args=[str(self.id)])



