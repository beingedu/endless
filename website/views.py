from django.core.mail import send_mail
from django.shortcuts import render

from website.models import Setting, FAQ


def home(request):
    return render(request, 'home.html', {})


def homes(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            message_phone,
            ['trecontainerpools@gmail.com'],
        )

        return render(request, 'home.html', {'message_name': message_name})

    else:
        return render(request, 'home.html', {})


def aboutus(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def team(request):
    return render(request, 'team.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            [''],
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'pricing.html', context)


def gallery(request):
    return render(request, 'gallery.html', {})


def faq(request):
    return render(request, 'faq.html')
