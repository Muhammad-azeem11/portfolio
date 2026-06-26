from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_list, name='education_list'),
]
