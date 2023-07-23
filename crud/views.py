from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib import messages
from .models import Employee
from django.views.generic import UpdateView, DeleteView

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request, 'crud/home.html', context)

def addEmployee(request):
    
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Employee Successfully')
            return redirect('home')
        else:
            messages.error(request, 'An Error Occured')
            return redirect('add_employee')
    
    else:
        form = EmployeeForm()
    return render(request, 'crud/add_employee.html', {'form':form})

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'dob', 'contact', 'email', 'address']
    success_url = '/'
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/'