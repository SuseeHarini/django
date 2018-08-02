# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import operator


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.response import TemplateResponse
from django.db.models import Q

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import EmployeeModel
from .forms import EmployeeForm


class EmployeeView(CreateView):
    model_class = EmployeeModel
    form_class = EmployeeForm
    success_url = reverse_lazy('thanks')
    initial = {'your_name': 'value'}
    template_name = 'employees/employee.html'

    def get(self, request, *args, **kwargs):
        model = self.model_class()
        return render(request, self.template_name, {'model': EmployeeModel})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('thanks/')
            else:
                form = EmployeeForm()
                return render(request, 'employee.html', {'form': form})

def emp_listview(request):
    template_name = 'employees/form.html'
    queryset = EmployeeModel.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def emp_form(request):
    return render(request, 'employees/search.html')

def emp_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        employees = EmployeeModel.objects.filter(Q(name__icontains=q) | Q(address__icontains=q) | Q(phone__icontains=q) | Q(dob__icontains=q) | Q(emp_id__icontains=q))
        return render(request, 'employees/search_result.html',
                      {'employees': employees, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
