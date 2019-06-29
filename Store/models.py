from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from Food.models import Food

class Manager(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)
	phone_num = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('manager-detail', args=[str(self.id)])


class Store(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	manager = models.OneToOneField(Manager,on_delete=models.CASCADE,null=True)
	foods = models.ManyToManyField(Food)
	branch_num = models.PositiveIntegerField()
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	pub_date = models.DateTimeField(auto_now=False)
	address = models.CharField(max_length=300)

	def __str__(self):
		return str(self.branch_num) + '  --- '  + (self.address)

	def get_absolute_url(self):
		return reverse('store-detail', args=[str(self.id)])

class Employee(models.Model):
	store = models.ForeignKey(Store,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)
	phone_num = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False)

	def __str__(self):
		return str(self.name) + '  --- '  + (self.address)

	def get_absolute_url(self):
		return reverse('employee-detail', args=[str(self.id)])




