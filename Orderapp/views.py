from django.shortcuts import render, redirect
from Orderapp.forms import OrderForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import smtplib


# Create your views here.

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            gmail_user = 'thisisadummyusername01@gmail.com'
            gmail_pwd = 'thisisadummypassword01'
            to = 'thisisadummyusername01@gmail.com'
            subject = 'Order'
            message = 'Order: ' + form.cleaned_data['what_are_you_ordering'] + 'Quantity: ' + str(form.cleaned_data['quantity']) + 'Name: ' + form.cleaned_data['last_name'] + form.cleaned_data['first_name'] + '\n Company: ' + form.cleaned_data['company'] + '\n Address: ' + form.cleaned_data['address'] + '\n Place of Delivery: ' + form.cleaned_data['place_of_delivery']
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + '\n'
            msg = header + '\n' + message + '\n\n'
            # ##---------------email is sent ----------------##
            smtpserver = smtplib.SMTP('smtp.gmail.com', 587)#587
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(gmail_user, gmail_pwd)
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()
            return render(request, 'thank_you.html')
        else:
            # if sum not equal... then redirect to custom url/page
            return HttpResponseRedirect('/')  # mention redirect url in argument
    else:
        form = OrderForm()
        return render(request, 'order_form.html', {'form': form})

    # to2 = [to]
    # send_mail(subject, message, gmail_user, to2, fail_silently=False, auth_user=gmail_user, auth_password=gmail_pwd)
    # send_mail(subject, message, gmail_user, to2, fail_silently=False)
