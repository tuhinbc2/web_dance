from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response

def handleFirstPage(request):
    t = Template("<h1> Hello {{name}} </h1>")
    c = Context({"name":"tuhin"})
    return HttpResponse(t.render(c))

def handleSecondPage(req):
    dpt = ['ios', 'win_desktop', 'web', 'test_automation', 'android', 'sdk', 'hr', 'cloud', 'bigdata']
    points = range(5)
    return render_to_response('first.html', locals())