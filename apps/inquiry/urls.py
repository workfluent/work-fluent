from django.urls import path
from .views import inquiry_form
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('', inquiry_form, name='inquiry_form'),
    path('thank-you/', TemplateView.as_view(template_name='inquiry/thank_you.html'), name='thank_you'),  # Thank you page
]
