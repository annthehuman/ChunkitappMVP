from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.contrib.sessions.models import Session

class background(models.Model):
	man = 'MAN'
	woman = 'WOMAN'
	other = 'OTHER'
	gender_choices = (
		(man, 'Mies'),
		(woman, 'Nainen'),
		(other, 'Muu'),
		)
	right = 'RIGHT'
	left = 'LEFT'
	both = 'BOTH'
	hands_choices = (
		(right, 'Oikeakätinen'),
		(left, 'Vasenkätinen'),
		(both, 'Ambidekstri / molempikätinen'),
		)
	primary = 'PRIMARY'
	basic = 'BASIC'
	mature = 'MATURE'
	othersec = 'OTHERSECONDARY'
	bachelor = 'BACHELOR'
	candidate = 'CANDIDATE'
	master = 'MASTER'
	diploma = 'DIPLOMA'
	di = 'DI'
	doctor = 'DOCTOR'
	polytech = 'POLYTECH'
	education_choices = (
		(primary, 'Peruskoulu'),
		(mature, 'Ylioppilastutkinto '),
		(othersec, 'Muu toisen asteen tutkinto'), 
		(candidate, 'Kandidaatin tutkinto'),
		(master, 'Maisterin tutkinto'),
		(diploma, 'Diplomi-insinööritutkinto'), 
		(doctor, 'Tohtorin tutkinto'),
		(polytech, 'Ammattikorkeakoulututkinto'),
		)
	degree_choices = (
		(basic, 'Peruskoulutus'),
		(mature, 'Ylioppilastutkinto'),
		(othersec, 'Muu toisen asteen tutkinto'),
		(bachelor, 'Amk-tutkinto'),
		(candidate, 'Kandidaatin tutkinto'),
		(master, 'Maisterin tutkinto'),
		(di, 'DI'),
		(doctor, 'Tohtorin tutkinto'),
		)
	yes = 'YES'
	no = 'NO'
	yes_no = (
		(yes, 'Kyllä'),
		(no, 'Ei'),
		)
	session_key = models.CharField(max_length=40)
	age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
	sex = models.CharField(max_length=6, choices=gender_choices)
	hand = models.CharField(max_length=28, choices=hands_choices)
	place = models.CharField(max_length=1000, default="nowhere")
	language = models.CharField(max_length=1000, default="none")
	other_languages = models.CharField(max_length=1000, default="no")
	use_language = models.CharField(max_length=1000, default="neither")
	education = models.CharField(max_length=14, choices=education_choices)
	major = models.CharField(max_length=1000, default="none")
	degree = models.CharField(max_length=14, choices=degree_choices)
	dyslexia = models.CharField(max_length=5, choices=yes_no)
	hearing = models.CharField(max_length=5, choices=yes_no)
	comments = models.TextField(default='nothing')

class feedback(models.Model):
	str_disagree = 'StrongleDisagree'
	disagree = 'Disagree'
	neither = 'NietherAgreeDisagree'
	agree = 'Agree'
	str_agree = 'StrongleAgree'
	opinion_choices = (
		(str_disagree, 'Vahvasti eri mieltä'),
		(disagree, 'Eri mieltä'),
		(neither, 'Ei samaa eikä eri mieltä'),
		(agree, 'Samaa mieltä'),
		(str_disagree, 'Vahvasti samaa mieltä'),	
		)
	bad = 'Bad'
	ok = 'Ok'
	good = 'Good'
	vgood = 'VGood'
	performance_choices = (
		(bad, 'Huono'),
		(ok, 'Kohtalainen'),
		(good, 'Hyvä'),
		(vgood, 'Todella hyvä'),
		)
	all_the_time = 'AllTheTime'
	most_of_the_time = 'MostOfTheTime'
	some_time = 'SomeTime'
	very_little_time = 'VeryLittleTime'
	not_at_all = 'NotAtAll'
	understanding_choices = (
		(all_the_time, 'Koko ajan'),
		(most_of_the_time, 'Suurimman osan ajasta'),
		(some_time, 'Jonkin verran ajasta'),
		(very_little_time, 'Hyvin vähän ajasta'),
		(not_at_all, 'En yhtään'),
		)
	session_key = models.CharField(max_length=40)
	instructions = models.CharField(max_length=25, choices=opinion_choices)
	doing = models.CharField(max_length=25, choices=opinion_choices)
	simple = models.CharField(max_length=25, choices=opinion_choices)
	demanding = models.CharField(max_length=25, choices=opinion_choices)
	pressure = models.CharField(max_length=25, choices=opinion_choices)
	fun = models.CharField(max_length=25, choices=opinion_choices)
	reflects = models.CharField(max_length=25, choices=opinion_choices)
	performance = models.CharField(max_length=25, choices=performance_choices)
	understanding = models.CharField(max_length=25, choices=understanding_choices)
	task = models.TextField(default='nothing')
	strategy = models.TextField(default='nothing')
	criteria = models.TextField(default='nothing')
	impression = models.TextField(default='nothing')
	comments = models.TextField(default='nothing') 


class test(models.Model):
	session_key = models.CharField(max_length=40)
	checkbox = models.TextField(default='nothing')
	index = models.IntegerField()
	question = models.CharField(max_length=10)

class sessions(models.Model):
	session_id = models.CharField(max_length=40)
	session_key = models.TextField(default='nothing')
	ip = models.CharField(max_length=400)