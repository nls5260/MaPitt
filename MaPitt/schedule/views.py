from django.shortcuts import render
from .models import Course, User

# Create your views here.
def index(request):
    context = {'course_list': Course.objects.all}
    return render(request, 'schedule/index.html', context)
