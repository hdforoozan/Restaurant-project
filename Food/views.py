from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
from .models import Food

class FoodListView(ListView):
	model = Food
	context_object_name = 'foods'


class FoodDetailView(DetailView):
	model = Food
	context_object_name = 'food'




