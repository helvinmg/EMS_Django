from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home',views.home,name='home'),
    path('employees',views.emp_list,name='employees'),
    path('about',views.about,name='about'),
]
