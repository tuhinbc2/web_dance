# -*- coding: utf-8 -*-
import datetime
import timeit
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import book,publisher,author

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def sum(req, a, b):
    return HttpResponse("sum is :" + str(int(a)+int(b)))

def dbtest(req):
    hi  = timeit.timeit("i=5;i**200")
    return HttpResponse("done " + str(hi))

def newword(req):
    return render_to_response('newword.html')

def dtest(req):
    p1 = publisher(name='tuhin', address='dhaka', city = 'dhaka', website='png.com')
    p1.save()

    p2 = publisher(name = 'mamun', address='kalampur', city = 'ksa')
    p2.save()

    time = timeit.timeit("from books.models import book,publisher,author;p2 = publisher(name = 'mamun', address='kalampur', city = 'ksa');p2.save()", number= 500)

    return HttpResponse("hello i'm fine time:" + str(time))    