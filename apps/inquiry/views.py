from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Inquiry

def inquiry_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        inquiry = Inquiry.objects.create(name=name, email=email, message=message)

        # Send email notification to admin
        send_mail(
            subject=f'New Inquiry from {name}',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email=None,  # Uses DEFAULT_FROM_EMAIL
            recipient_list=['admin@example.com'],  # Replace with admin email
        )

        # Send confirmation email to the user
        send_mail(
            subject='Thank you for your inquiry',
            message='We have received your inquiry and will get back to you soon.',
            from_email=None,  # Uses DEFAULT_FROM_EMAIL
            recipient_list=[email],
        )

        return HttpResponse("Thank you for your inquiry!")
    return render(request, 'inquiry_form.html')
