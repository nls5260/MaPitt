from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
     # ex: /schedule/
    path('', views.index, name='index'),

]
