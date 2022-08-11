from django.http import Http404
from django.shortcuts import render
from .models import Employee

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees':employees})

def employee_detail(request, employee_id):
    try:
        employee = Employee.objects.get(id = employee_id)
    except Employee.DoesNotExist:
        raise Http404
    return render(request, 'employee_detail.html', {'employee':employee})