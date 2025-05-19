import logging  # Import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError  # Import ValidationError
from .models import Inquiry

logger = logging.getLogger(__name__)  # Initialize logger

def inquiry_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name', "")
        company_website = request.POST.get('company_website', "")
        budget = request.POST.get('budget')
        message = request.POST.get('message')

        # Validate message word count
        if len(message.split()) > 200:
            messages.error(request, "Message cannot exceed 200 words.")
            return redirect('inquiry_form')

        # Save inquiry to the database
        inquiry = Inquiry(
            name=name,
            email=email,
            company_name=company_name,
            company_website=company_website,
            budget=budget,
            message=message,
        )
        try:
            inquiry.clean()  # Validate using the model's clean method
            inquiry.save()
        except ValidationError as e:
            messages.error(request, " ".join(e.messages))  # Ensure error messages are user-friendly
            return redirect('inquiry_form')

        # Send email notification to admin
        try:
            admin_email_body = render_to_string('emails/admin_notification.html', {
                'name': name,
                'email': email,
                'company_name': company_name,
                'company_website': company_website,
                'budget': budget,
                'message': message,
            })
            send_mail(
                subject=f'New Inquiry from {name}',
                message=admin_email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin[1] for admin in settings.ADMINS],
            )
            logger.info("Admin notification email sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send admin notification email: {e}")

        # Send confirmation email to the user
        try:
            user_email_body = render_to_string('emails/user_confirmation.html', {
                'name': name,
            })
            send_mail(
                subject='Thank you for your inquiry',
                message=user_email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
            logger.info("User confirmation email sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send user confirmation email: {e}")

        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect('thank_you')  # Redirect to the thank you page
    return render(request, 'index.html')  # Ensure the correct template is rendered
