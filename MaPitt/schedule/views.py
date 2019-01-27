from django.shortcuts import render
from .models import Course, User
from django.http import HttpResponse, HttpResponseRedirect


def list(request):
    context = {'course_list': Course.objects.all}
    return render(request, 'schedule/list.html', context)

def index(request):
    context = {}
    return render(request, 'schedule/index.html', context)
