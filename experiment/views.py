from django.shortcuts import render, redirect


def introduction(request):
    return render(request, 'experiment/introduction.html', {})

def consent(request):
    return render(request, 'experiment/consent.html', {})

def questionnaire(request):
    return render(request, 'experiment/questionnaire.html', {})

def practice13(request):
    return render(request, 'experiment/practice13.html', {})

def thanks(request):
    return render(request, 'experiment/thanks.html', {})