from django.shortcuts import render
from .models import Store, Employee, Manager
from Food.models import Food
import datetime
from django.views.generic import TemplateView,DetailView,ListView

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['most_sell_foods'] = Food.objects.filter(name='Pizza')
	    context['newest_foods'] = Food.objects.filter(pub_date__gte=datetime.date.today())
	    return context

class StoreListView(ListView):
	model = Store
	context_object_name = 'stores'

class StoreDetailView(DetailView):
	model = Store
	context_object_name = 'store'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['foods'] = Food.objects.filter(store__id=self.kwargs['pk'])
	    context['employees'] = Employee.objects.filter(store__id=self.kwargs['pk'])
	    emps = Employee.objects.filter(store__id=self.kwargs['pk'])
	    return context
