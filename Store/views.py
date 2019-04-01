from django.shortcuts import render
from .models import Store, Employee, Manager
from Food.models import Food
from django.views.generic import TemplateView,DetailView,ListView

class HomePageView(TemplateView):
	template_name = 'home.html'

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
	    for e in emps:
	    	print(e.name)
	    return context
