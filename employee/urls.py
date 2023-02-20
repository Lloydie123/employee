from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'employee'
urlpatterns = [
   
     # Path for employees
     path('index/', views.ListView.as_view(), name='index'),
     path('create/', views.CreateEmployee.as_view(), name='create'),
     path('<int:pk>/update/', views.UpdateEmployee.as_view(), name='update'),
     path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete'),
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path('', TemplateView.as_view(template_name='employee/base.html'), name='base'),
     
     #Path for department
     
     path('create_department/',views.MemberCreate.as_view(),name='MemberCreate'),
     path('emp', views.emp),  
     path('show',views.show),  
     path('edit/<int:id>', views.edit), 
     path('update/<int:id>', views.update),  
     path('delete/<int:id>', views.destroy),  
     
     
     path('new', views.book_create, name='book_create'),
     path('list', views.book_list, name='book_list'),
     path('<int:pk>/edit', views.book_edit, name='book_edit'),
     path('<int:pk>/delete', views.book_delete, name='book_delete'),
    
]
