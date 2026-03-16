from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h2>hello from EMS</h2>")

def emp_list(request):
    #records coming from db
    emps=[{'name':'Varun','desg':'intern','salary':15000},{'name':'vinu','desg':'Jr Developer','salary':45000}]
    return render(request,"emp_list.html",{'emps':emps})
