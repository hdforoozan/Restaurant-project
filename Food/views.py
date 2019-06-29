from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView, CreateView,DeleteView,UpdateView
from .models import Food
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class FoodListView(LoginRequiredMixin, ListView):
	model = Food
	context_object_name = 'foods'


class FoodDetailView(LoginRequiredMixin, DetailView):
	model = Food
	context_object_name = 'food'


class FoodCreateView(LoginRequiredMixin, CreateView):
	model = Food
	fields = ['user','name','description','pub_date','image','price','detail']


class FoodUpdateView(LoginRequiredMixin, UpdateView):
	model = Food
	fields = ['name','description','image','price','detail']
	context_object_name = 'food'
	template_name = 'Food/food_update_form.html'

class FoodDeleteView(LoginRequiredMixin, DeleteView):
	model = Food
	success_url = reverse_lazy('food-list')
	context_object_name = 'food'







