from django.test import TestCase
from .models import Store, Employee, Manager
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class ManagerTestCase(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'testpasswrod',
			is_staff = True,
			is_superuser = True,
			)
		self.client.login(username='testuser',password='testpasswrod')
		self.manager = Manager.objects.create(
			pk = 1,
			name = 'Abbas',
			address = 'Tehran , No2',
			phone_num = '09123654789',
			pub_date = datetime.now(),
			)

	def test_manager_detail_view(self):
		response = self.client.get(reverse('manager-detail', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Tehran , No2')
		self.assertTemplateUsed(response, 'Store/manager_detail.html')









