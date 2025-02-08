from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def graphs(request):
  template = loader.get_template('doc.html')
  return HttpResponse(template.render())
