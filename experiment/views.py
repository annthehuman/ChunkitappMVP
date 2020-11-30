from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import checkboxfield
from django.http import HttpResponse
from .models import background, feedback, test, sessions
from .forms import backgroundForm, feedbackForm
import uuid
import random

def introduction(request):
	return render(request, 'experiment/introduction.html', {})

def get_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def consent(request):
	if request.method == 'POST':
		if request.POST['consent'] == "Olen samaa mieltä":
			ip = get_ip(request)
			print(ip)
			if sessions.objects.filter(ip=str(ip)):
				for i in sessions.objects.filter(ip=str(ip)):
					print(i.ip)
				print('IP found')
				return redirect('passed')
			if request.session.session_key:
				return redirect('passed')
			else:
				global x
				x = str(uuid.uuid4())
				request.session.set_expiry(2000)
				request.session[x]=x
				#session = request.session.session_key
				print(request.session[x])
				request.session.save()
				session = request.session.session_key
				print(request.session.session_key)
				sessions.objects.create(
					session_id = request.session[x],
					session_key = session,
					ip = ip
					)
			#print(request.session[x])
			return redirect('questionnaire')
		elif request.POST['consent'] == "En ole samaa mieltä":
			return redirect('thanks')
	return render(request, 'experiment/consent.html', {})

def you_passed(request):
	return render(request, 'experiment/passed.html', {})

def questionnaire(request):
	form = backgroundForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newanswer = form.save(commit=False)
			newanswer.session_key = request.session.session_key
			newanswer.save()
			return redirect('training1')
	return render(request, 'experiment/questionnaire.html', {'form': form})


def data(request):
	if request.method == 'POST':
		checkboxes = request.POST.getlist('check[]')
		index = request.POST['index']
		session = request.session.session_key
		question = request.POST['question']
		test.objects.create(
			session_key = session,
			checkbox = checkboxes,
			index = index,
			question = question
			)
		print(checkboxes, question, session, index)
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
	form = feedbackForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newanswer = form.save(commit=False)
			newanswer.session_key = request.session.session_key
			newanswer.save()
	return render(request, 'experiment/feedback.html', {'form': form})

def end(request):
	return render(request, 'experiment/end.html', {})
