from django.shortcuts import render
from .models import Store, Employee, Manager
from Food.models import Food
import datetime
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView, CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['most_sell_foods'] = Food.objects.filter(name__icontains='p')
	    context['cheapest_foods'] = Food.objects.filter(price__lte=10)
	    return context


##############################################################
# Store Model Views
##############################################################


class StoreListView(LoginRequiredMixin, ListView):
	model = Store
	context_object_name = 'stores'

class StoreDetailView(LoginRequiredMixin, DetailView):
	model = Store
	context_object_name = 'store'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['foods'] = Food.objects.filter(store__id=self.kwargs['pk'])
	    context['employees'] = Employee.objects.filter(store__id=self.kwargs['pk'])
	    u = Employee.objects.filter(store__id=self.kwargs['pk'])
	    for i in u:
	    	print(i.pk)
	    return context


class StoreCreateView(LoginRequiredMixin, CreateView):
	model = Store
	fields = ['user','manager','foods','branch_num','image','pub_date','address']


class StoreUpdateView(LoginRequiredMixin, UpdateView):
	model = Store
	fields = ['manager','foods','branch_num','image','address']
	context_object_name = 'store'
	template_name = 'Store/store_update_form.html'


class StoreDeleteView(LoginRequiredMixin, DeleteView):
	model = Store
	success_url = reverse_lazy('store-list')
	context_object_name = 'store'

##############################################################
# Manager Model Views
###############################################################


class ManagerDetailView(LoginRequiredMixin, DetailView):
	model = Manager
	context_object_name = 'manager'



class ManagerUpdateView(LoginRequiredMixin, UpdateView):
	model = Manager
	fields = ['name','address','phone_num']
	context_object_name = 'manager'
	template_name = 'Store/manager_update_form.html'


class ManagerDeleteView(LoginRequiredMixin, DeleteView):
	model = Manager
	success_url = reverse_lazy('store-list')
	context_object_name = 'manager'


##############################################################
# Employee Model Views
###############################################################



class EmployeeDetailView(LoginRequiredMixin, DetailView):
	model = Employee
	context_object_name = 'employee'


class EmployeeCreateView(LoginRequiredMixin, CreateView):
	model = Employee
	fields = ['store','name','address','phone_num','pub_date']


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
	model = Employee
	fields = ['name','address','phone_num']
	context_object_name = 'employee'
	template_name = 'Store/employee_update_form.html'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
	model = Employee
	success_url = reverse_lazy('store-detail')
	context_object_name = 'employee'