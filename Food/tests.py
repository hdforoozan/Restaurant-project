from django.test import TestCase
from .models import Food
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime

class FoodTestCase(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'secret',
			)
		self.client.login(username = 'testuser',password = 'secret')

		# self.food = Food.objects.create(
		# 	user = self.user,
		# 	name = 'spagetti',
		# 	description = 'This is a good food',
		# 	pub_date = datetime.now(),
		# 	price = 10,
		# 	detail = 'meat,vegetable,water'
		# 	)

	def test_food_list_view(self):
		response = self.client.get(reverse('food-list'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'Food/food_list.html')
		#print(response.content)
		print(response.context)
		#self.assertContains(response, )

	# def test_food_detail_view(self):
	# 	response = self.client.get(reverse('food-detail', args='1'))
	# 	self.assertEqual(response.status_code,200)