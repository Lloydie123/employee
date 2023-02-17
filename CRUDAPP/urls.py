from django.urls import path
from . import views

urlpatterns = [
    
    # '' Indicates as the home page or landing page  
  
    # For the functions
    path('insert/', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
    path('', views.home),
 
    path("simple_function", views.simple_function),
   ]