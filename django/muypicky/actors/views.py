# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.response import TemplateResponse
from django.db.models import Q

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Actor
from .forms import ActorForm


class ActorView(CreateView):
    model_class = Actor
    form_class = ActorForm
    success_url = reverse_lazy('thanks')
    initial = {'your_name': 'value'}
    template_name = 'actors/actor.html'

    def get(self, request, *args, **kwargs):
        model = self.model_class()
        return render(request, self.template_name, {'model': Actor})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ActorForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('thanks/')
            else:
                form = ActorForm()
                return render(request, 'actor.html', {'form': form})

def act_listview(request):
    template_name = 'actors/actor_form.html'
    queryset = Actor.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def act_form(request):
    return render(request, 'actors/actor_search.html')

def act_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        actors = Actor.objects.filter(Q(name__icontains=q) | Q(surname__icontains=q) | Q(age__icontains=q))
        return render(request, 'actors/actor_search_result.html',
                      {'actors': actors, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
