from django.contrib import admin
from .models import Store, Manager, Employee

admin.site.register(Manager)

class EmployeeInline(admin.TabularInline):
	model = Employee
	min_num = 1
	extra = 1

class StoreAdmin(admin.ModelAdmin):
	inlines = [EmployeeInline]
	search_field = ['address']
	list_display = ['address', 'branch_num']

admin.site.register(Store,StoreAdmin)

