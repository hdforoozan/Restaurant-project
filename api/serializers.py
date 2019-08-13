from rest_framework import serializers
from django.contrib.auth import get_user_model
from Food.models import Food
from Store.models import Store, Manager, Employee

class FoodSerializer(serializers.ModelSerializer):
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	class Meta:
		model = Food
		fields = ('id','user','name','description','image','pub_date','price','detail')


class StoreSerializer(serializers.ModelSerializer):
	employees = serializers.StringRelatedField(many=True)
	foods = serializers.StringRelatedField(many=True)
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)

	class Meta:
		model = Store
		fields = ('id','user', 'manager','foods','branch_num','image','pub_date','address', 'employees')


class ManagerSerializer(serializers.ModelSerializer):
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)

	class Meta:
		model = Manager
		fields = ('id','name','address','phone_num','pub_date')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id','username')
