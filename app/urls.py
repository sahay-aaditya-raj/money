from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='home'),
    path('new-entry/', views.new_entry, name='new-entry'),
    path('view/', views.view, name='view'),
    path('data/<str:pk>/', views.view_data, name='data'),
    path('delete-data/<str:pk>/', views.delete_data, name='delete')
]
