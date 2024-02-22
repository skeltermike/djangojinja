from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='about us.html')


def contact(request):
    return render(request, template_name='contact.html')


def gallery(request):
    return render(request, template_name='gallery.html')
