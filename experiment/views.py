from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import checkboxfield
from django.http import HttpResponse
import uuid
import random

def introduction(request):
	return render(request, 'experiment/introduction.html', {})

def consent(request):
	if request.method == 'POST':
		if request.POST['consent'] == "Olen samaa mieltä":
			global x
			x = str(uuid.uuid4())
			request.session.set_expiry(2000)
			request.session[x]=x
			#print(request.session[x])
			return redirect('questionnaire')
		elif request.POST['consent'] == "En ole samaa mieltä":
			return redirect('thanks')
	return render(request, 'experiment/consent.html', {})

def questionnaire(request):
	return render(request, 'experiment/questionnaire.html', {})

def data(request):
	if request.method == 'POST':
		chexboxes = request.POST.getlist('check[]')
		index = request.POST['index']
		session = request.session[x]
		question = request.POST['question']
		#print(chexboxes, question, session, index)
		return HttpResponse('')


def training1(request):
	return render(request, 'experiment/training1.html', {})


def training2(request):
	return render(request, 'experiment/training2.html', {})

def training3(request):
	return render(request, 'experiment/training3.html', {})

def trainingcompleted(request):
	if request.method == 'POST':
		#print(request.POST['next'])
		if request.POST['next'] == 'Jatka':
			order = [i for i in range(4,44)]
			random.shuffle(order)
			request.session['order'] = order
			return redirect('get_challange')	
	return render(request, 'experiment/trainingcompleted.html', {})

def confirm(request):
    return render(request, 'experiment/challange.html', {'order': request.session['order']})


def challange(request):
	print(request.session)
	return render(request, 'experiment/challange.html', {})

def thanks(request):
    return render(request, 'experiment/thanks.html', {})

def taskcompleted(request):
	return render(request, 'experiment/taskcompleted.html', {})

def feedback(request):
	return render(request, 'experiment/feedback.html', {})

def end(request):
	return render(request, 'experiment/end.html', {})
