from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from books.models import Publisher

def hello(request):
    return HttpResponse("Hello world")

my_homepage_view = hello

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', locals())

def first_app(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'first_app.html', {'publisher_list': publisher_list})


