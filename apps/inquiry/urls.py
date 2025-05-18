from django.urls import path
from .views import inquiry_form

urlpatterns = [
    path('inquiry/', inquiry_form, name='inquiry_form'),
]
