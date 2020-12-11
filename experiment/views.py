from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import checkboxfield
from django.http import HttpResponse
from .models import background, feedback, test, sessions
from .forms import backgroundForm, feedbackForm
import uuid
import random
from django.contrib.sessions.models import Session
from operator import itemgetter
import csv
import os
from django.utils import timezone
import datetime

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
		if request.POST['consent'] == "Hyväksyn":
			ip = get_ip(request)
			#print(ip)
			#if sessions.objects.filter(ip=str(ip)):
				#for i in sessions.objects.filter(ip=str(ip)):
					#print(i.ip)
				#print('IP found')
			#if request.session.session_key:
				#return redirect('passed')
			#else:
			if request.session.session_key:
				session_key = request.session.session_key
				session = Session.objects.get(session_key=session_key)
				#print(session)
				Session.objects.filter(session_key=session).delete()
			global x
			x = str(uuid.uuid4())
			request.session.set_expiry(5400)
			request.session[x]=x
			#print(request.session[x])
			request.session.save()
			session = request.session.session_key
			publish_date = datetime.datetime.now()
			#print(publish_date)
			#print(request.session.session_key)
			sessions.objects.create(
				session_id = request.session[x],
				session_key = session,
				ip = ip,
				published_date = publish_date
				)
			#print(request.session[x])
			return redirect('questionnaire')
		elif request.POST['consent'] == "En hyväksy":
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
		#print(checkboxes, question, session, index)
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
			return redirect('get_challenge')	
	return render(request, 'experiment/trainingcompleted.html', {})

def confirm(request):
    return render(request, 'experiment/challenge.html', {'order': request.session['order']})


def challenge(request):
	#print(request.session)
	return render(request, 'experiment/challenge.html', {})

def thanks(request):
    return render(request, 'experiment/thanks.html', {})

def taskcompleted(request):
	return render(request, 'experiment/taskcompleted.html', {})

def feedbackQ(request):
	form = feedbackForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newanswer = form.save(commit=False)
			newanswer.session_key = request.session.session_key
			newanswer.save()
			return redirect('end')
	return render(request, 'experiment/feedback.html', {'form': form})

def end(request):
	return render(request, 'experiment/end.html', {})



def results(request):
	f_texts = open('texts.txt', 'r')
	texts = [[0 for i in range(0, 3)] for n in range (0, 43)]
	ii = 0
	for line in f_texts:
		n = line.split()
		texts[ii][0] = int(n[0])
		texts[ii][1] = n[1]
		texts[ii][2] = int(n[2])
		ii += 1
	#sprint(texts)
	f_texts.close()
	checkboxes = list(test.objects.all().values_list('checkbox'))
	session = test.objects.all().values_list('session_key')
	text_from_user = test.objects.all().values_list('index')
	session_time = list(sessions.objects.all().values_list('published_date'))
	session_key_time = list(sessions.objects.all().values_list('session_key'))
	session_list = []
	session_dict = {}
	time = []
	for i in range(len(session_key_time)):
		t = [session_time[i][0], session_key_time[i][0]]
		time.append(t)
	#print(time, session_time[i][0])
	for i in session:
		for n in i:
			session_list.append(n)
			session_dict.setdefault(n)
	#print(len(session_dict))
	text_from_user_list = []
	for i in text_from_user:
		for n in i:
			text_from_user_list.append(n)
	check_list = []
	for i in checkboxes:
		for n in i:
			k_list = []
			for k in n.split(','):
				k = k.replace("'", "").replace('[', '').replace(']', '')
				if k !=  '':
					k = int(k)
				k_list.append(k)
			check_list.append(k_list)
	results_dict = dict()
	for i in range(len(text_from_user_list)):
		resent_results = []
		for n in range (texts[text_from_user_list[i]-1][2]-1):
			if n in check_list[i]:
				resent_results.append(1)
			else:
				resent_results.append(0)
		results = [session_list[i], resent_results]
		results_dict.setdefault(text_from_user_list[i], []).append(results)
		#print([text_from_user_list[i]-1], results)
	#print(results_dict)
	#print(list(results_dict.keys()))
	texts_lists_table = []
	length = 0
	for item in list(results_dict.keys()):
		text_lists_table = []
		for j in range(texts[item-1][2]-1):
			t = item, str(texts[item-1][1].replace('.mp3', '')), j+1
			text_lists_table.append(t)
			length += 1
		texts_lists_table.append(text_lists_table)
	#print(len(list(results_dict.values())[0]))
	length_dict = []
	max_length = len(session_dict)
	#print(texts_lists_table)
	table = [[0 for i in range(max_length+1)] for n in range(length+2)]
	#print(list(results_dict.values())[0])
	table[0][0] = ()
	table[1][0] = ()
	#print(list(session_dict.keys())[2])
	for n in range(1, max_length+1):
		table[0][n] = list(session_dict.keys())[n-1]
	for n in range(1, max_length+1):
		for i in range(len(time)):
			if time[i][1] == table[0][n] and type(time[i][0]) != type(None):
				#print(type(time[i][0]), 1)
				table[1][n] = time[i][0].strftime("%m-%d-%Y\n%H:%M:%S") 
	#print(type((time[1][0])) == type(None))
	#print(results_dict)
	i = 2
	for j in range(len(texts_lists_table)):
		for k in range(len(texts_lists_table[j])):
			table[i][0]=texts_lists_table[j][k] 
			for n in range(1, max_length+1):
				for res in range(len(list(results_dict.values())[j])):
					#print(table[0][n], list(results_dict.values())[j][res][0])
					if table[0][n] == list(results_dict.values())[j][res][0]:
						table[i][n] = list(results_dict.values())[j][res][1][k]
			i += 1
	print(len(table))
	table = sorted(table, key=lambda x: x[0])
	table[0][0] = ''
	table[1][0] = ''
	for n in range(1, max_length+1):
		table[0][n] = table[0][n][:5]
	l = (length+1)
	w = (max_length+1)
	with open(os.path.join('experiment/static/', 'out.csv'), 'w', newline='') as of:
		wRt = csv.writer(of)
		wRt.writerows(table)
	if len(table) <= 2:
		data = 'No data'
	else:
		data = ''
	#print(results_dict)
	#print(list(results_dict.values())[0][0][1])
	return render(request, 'experiment/results.html', {'o': table, 'length': l, 'width': w, 'data': data})


def questions(request):
	question = test.objects.all().values_list('question')
	session = test.objects.all().values_list('session_key')
	text_from_user = test.objects.all().values_list('index')
	quests = [[0 for i in range(2)] for j in range(43)]
	question_list = []
	for i in question:
		for n in i:
			question_list.append(n)
	session_list = []
	session_dict = {}
	for i in session:
		for n in i:
			session_list.append(n)
			session_dict.setdefault(n)
	text_from_user_list = []
	for i in text_from_user:
		for n in i:
			text_from_user_list.append(n)
	ii = 0
	with open('quest.txt', 'r') as questions:
		for line in questions:
			line = line.split() 
			quests[ii][0] = line[0]
			quests[ii][1] = ' '.join(line[1:])
			ii += 1
	question_table = [[0 for i in range(len(session_dict)+1)] for j in range(44)]
	for i in range(1, len(session_dict)+1):
		question_table[0][i] = list(session_dict.keys())[i-1]
	for i in range(1, 44):
		question_table[i][0] = quests[i-1]
	for i in range(len(session_list)):
		for j in range(len(session_dict)+1):
			if session_list[i] == question_table[0][j]:
				#print(session_list[i])
				for k in range(1,len(question_table)):
					#print(question_table[k][j])
					if int(question_table[k][0][0]) == int(text_from_user_list[i]):
						question_table[k][j] = question_list[i]
	for n in range(1, len(session_dict)+1):
		question_table[0][n] = question_table[0][n][:5]

	import re
	question_table[0][0] =''
	for n in range(1, len(question_table)):
		question_table[n][0] = re.sub(r"[\[\]']", '', str(question_table[n][0]))
	with open(os.path.join('experiment/static/', 'questions.csv'), 'w', newline='') as of:
		wRt = csv.writer(of)
		wRt.writerows(question_table)
	return render(request, 'experiment/questions.html', {'question' : question_table})

def backgroundRES(request):
	try:
		table = background.objects.all().values()
		table_list = []
		#table.append()
		for tab in table:
			table_list.append(list(tab.values()))
		tab_keys = list(tab.keys())
		background_table = [[0 for i in range(len(tab_keys))] for j in range(len(table_list)+1)]
		for n in range(len(tab_keys)):
			background_table[0][n] = tab_keys[n]
			for k in range(1, len(table_list)+1):
				background_table[k][n] = table_list[k-1][n]
		for k in range(1, len(table_list)+1):
			background_table[k][1] = background_table[k][1][:5]
		with open(os.path.join('experiment/static/', 'background.csv'), 'w', newline='') as of:
			wRt = csv.writer(of)
			wRt.writerows(background_table)	
		no_data = ''
	except:
		background_table = ''
		no_data = 'No data'
	return render(request, 'experiment/background_results.html', {'table': background_table, 'data': no_data})

def feedbackRES(request):
	try:
		table = feedback.objects.all().values()
		table_list = []
		#table.append()
		for tab in table:
			table_list.append(list(tab.values()))
		tab_keys = list(tab.keys())
		feedback_table = [[0 for i in range(len(tab_keys))] for j in range(len(table_list)+1)]
		for n in range(len(tab_keys)):
			feedback_table[0][n] = tab_keys[n]
			for k in range(1, len(table_list)+1):
				feedback_table[k][n] = table_list[k-1][n]
		for k in range(1, len(table_list)+1):
			feedback_table[k][1] = feedback_table[k][1][:5]
		with open(os.path.join('experiment/static/', 'feedback.csv'), 'w', newline='') as of:
			wRt = csv.writer(of)
			wRt.writerows(feedback_table)	
		no_data = ''
	except:
		feedback_table = ''
		no_data = 'No data'
	return render(request, 'experiment/feedback_results.html', {'table': feedback_table, 'data': no_data})