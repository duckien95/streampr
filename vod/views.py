# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from django.shortcuts import render

# Create your views here.
def hello(request):
    #return HttpResponse("Hello, world. You're at the hello index.")
    return render(request, 'streamvod.html')
    #return render_to_response('streamvod.html')
    #return HttpResponse(loader.get_template("streamvod.html").render),
