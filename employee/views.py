from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def emp_list(request):
    #records coming from db
    emps=Employee.objects.all()
    return render(request,"emp_list.html",{'emps':emps})
