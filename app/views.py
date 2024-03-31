from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse

# Create your views here.
class IndexView(TemplateView):
    template_name ='index.html'