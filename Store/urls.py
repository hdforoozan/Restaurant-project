from django.urls import path
from .views import (StoreListView, StoreDetailView,StoreUpdateView,
					StoreDeleteView,StoreCreateView,
					ManagerDetailView,ManagerUpdateView,
					ManagerDeleteView
					)


urlpatterns = [
	path('', StoreListView.as_view(), name='store-list'),
	path('<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
	path('add/', StoreCreateView.as_view(), name='store-add'),
	path('<int:pk>/update/', StoreUpdateView.as_view(), name='store-update'),
	path('<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),
	path('manager/<int:pk>', ManagerDetailView.as_view(), name='manager-detail'),
	path('manager/<int:pk>/update/', ManagerUpdateView.as_view(), name='manager-update'),
	path('manager/<int:pk>/delete/', ManagerDeleteView.as_view(), name='manager-delete'),


]

