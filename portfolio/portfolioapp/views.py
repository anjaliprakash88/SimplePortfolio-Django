from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def experience(request):
    return render(request, 'experience.html')


def skills(request):
    return render(request, 'skills.html')


def contact(request):
    return render(request, 'contact.html')