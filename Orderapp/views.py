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
            gmail_user = 'genmerchorder@gmail.com'
            gmail_pwd = 'thisisadummypassword01'
            to = 'mr.genmerch@gmail.com'# actual is mr.genmerch@gmail.com
            subject = 'Order'
            message = ' Order: ' + form.cleaned_data['what_are_you_ordering'] + '\n Quantity: ' + str(form.cleaned_data['quantity']) + '\n Name: ' + form.cleaned_data['last_name'] + ', ' + form.cleaned_data['first_name'] + '\n Email: ' + form.cleaned_data['email'] + '\n Company: ' + form.cleaned_data['company'] + '\n Address: ' + form.cleaned_data['address'] + '\n Place of Delivery: ' + form.cleaned_data['place_of_delivery']
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + '\n'
            msg = header + '\n' + message + '\n\n'
            # ##---------------email is sent ----------------##
            smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)#587 for non ssl or 465
            smtpserver.ehlo()
            #smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(gmail_user, gmail_pwd)
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()
            # ##---------------reply----------------##
            to = form.cleaned_data['email']
            subject = 'Order'
            message = 'Thank you for placing your order!\n Order: ' + form.cleaned_data['what_are_you_ordering'] + '\n Quantity: ' + str(form.cleaned_data['quantity']) + '\n Name: ' + form.cleaned_data['last_name'] + ', ' + form.cleaned_data['first_name'] + '\n Company: ' + form.cleaned_data['company'] + '\n Address: ' + form.cleaned_data['address'] + '\n Place of Delivery: ' + form.cleaned_data['place_of_delivery'] + '\n \nIf you have any questions or concerns please contact us at mr.genmerch@gmail.com'
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + '\n'
            replymsg = header + '\n' + message + '\n\n'

            # ##---------------reply is sent ----------------##
            smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # 587 for non ssl or 465
            smtpserver.ehlo()
            # smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(gmail_user, gmail_pwd)
            smtpserver.sendmail(gmail_user, to, replymsg)
            smtpserver.close()
            form = OrderForm()
            context = {
                'form': form,
            }
            return render(request, 'order_form.html', context)
        else:
            # if sum not equal... then redirect to custom url/page
            return HttpResponseRedirect('/')  # mention redirect url in argument
    else:
        form = OrderForm()
        return render(request, 'order_form.html', {'form': form})

    # to2 = [to]
    # send_mail(subject, message, gmail_user, to2, fail_silently=False, auth_user=gmail_user, auth_password=gmail_pwd)
    # send_mail(subject, message, gmail_user, to2, fail_silently=False)
