# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.response import TemplateResponse
from django.db.models import Q

from django.views.generic import CreateView
from django.urls import reverse_lazy
from books.models import Book
from .forms import BookForm


class BookView(CreateView):
    model_class = Book
    form_class = BookForm
    success_url = reverse_lazy('thanks')
    initial = {'title': 'value'}
    template_name = 'books/book.html'

    def get(self, request, *args, **kwargs):
        model = self.model_class()
        return render(request, self.template_name, {'model': Book})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('thanks/')
            else:
                form = BookForm()
                return render(request, 'book.html', {'form': form})

def book_listview(request):
    template_name = 'books/book_form.html'
    queryset = Book.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q) | Q(published__icontains=q))
        return render(request, 'books/search_results.html',
                      {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
