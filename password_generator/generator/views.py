from django.shortcuts import render
import random


def home(request):

    context = {
        'weak_range': range(6,16),
        'strong_range': range(16,129),
        'unbelievable_range': [256,512,1024,2048],
    }

    return render(request, 'generator/home.html', context)


def password(request):

    lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
    upper_case_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    length = int(request.GET.get('length',16))

    available_chars = lower_case_letters

    if request.GET.get('uppercase'):
        available_chars += upper_case_letters

    if request.GET.get('numbers'):
        available_chars += numbers

    if request.GET.get('symbols'):
        available_chars += symbols
    
    password = ''
    for l in range(length):
        password += random.choice(available_chars)

    return render(request, 'generator/password.html', {'password':password})