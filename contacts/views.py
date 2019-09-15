from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


# Create your views here.


def contact(request):
    print(request.path)
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_name = request.POST['listing']
        user_name = request.POST['name']
        user_id = request.POST['user_id']
        user_email = request.POST['email']
        user_phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        print(listing_id, listing_name, user_name, user_id, user_email, user_phone, message)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect("/listings/"+listing_id)

        contact_data = Contact(
            listing = listing_name,
            listing_id = listing_id,
            name = user_name,
            email = user_email,
            phone = user_phone,
            message = message,
            user_id = user_id
        )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon!")
        contact_data.save()

        # send_mail(
        #     'Properly listing inquiry',
        #     'There has been an inquiry for ' + listing_name,
        #     'neil.flowler@gmail.com',
        #     [realtor_email, 'neil.flowler@gmail.com'],
        #     fail_silently=False

        # )

        return redirect("/listings/"+listing_id)