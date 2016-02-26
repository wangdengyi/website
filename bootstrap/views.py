from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from  django.utils import timezone
# Create your views here.

def Index(request):
    t = timezone.now()
    template = loader.get_template('bootstrap/index.html')
    context = {'datetime' : t}
    return HttpResponse(template.render(context,request))
