from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.contrib.sessions.models import Session

class background(models.Model):
	man = 'Mies'
	woman = 'Nainen'
	other = 'Muu'
	gender_choices = (
		(man, 'Mies'),
		(woman, 'Nainen'),
		(other, 'Muu'),
		)
	right = 'Oikeakatinen'
	left = 'Vasenkatinen'
	both = 'Both'
	hands_choices = (
		(right, 'Oikeakätinen'),
		(left, 'Vasenkätinen'),
		(both, 'Ambidekstri / molempikätinen'),
		)
	primary = 'Peruskoulu'
	basic = 'Peruskoulutus'
	mature = 'Ylioppilastutkinto'
	othersec = 'MuuToisenAsteenTutkinto'
	bachelor = 'AmkTutkinto'
	candidate = 'KandidaatinTutkinto'
	master = 'MaisterinTutkinto'
	diploma = 'DiplomiInsinooritutkinto' 
	di = 'DI'
	doctor = 'TohtorinTutkinto'
	polytech = 'Ammattikorkeakoulututkinto'
	none = ''
	education_choices = (
		(primary, 'Peruskoulu'),
		(mature, 'Ylioppilastutkinto'),
		(othersec, 'Muu toisen asteen tutkinto'), 
		(candidate, 'Kandidaatin tutkinto'),
		(master, 'Maisterin tutkinto'),
		(diploma, 'Diplomi-insinööritutkinto'), 
		(doctor, 'Tohtorin tutkinto'),
		(polytech, 'Ammattikorkeakoulututkinto'),
		)
	degree_choices = (
		(none, '---------'),
		(basic, 'Peruskoulutus'),
		(mature, 'Ylioppilastutkinto'),
		(othersec, 'Muu toisen asteen tutkinto'),
		(bachelor, 'Amk-tutkinto'),
		(candidate, 'Kandidaatin tutkinto'),
		(master, 'Maisterin tutkinto'),
		(di, 'DI'),
		(doctor, 'Tohtorin tutkinto'),
		)
	yes = 'Kylla'
	no = 'Ei'
	yes_no = (
		(yes, 'Kyllä'),
		(no, 'Ei'),
		)
	session_key = models.CharField(max_length=40)
	ika = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
	sukupuoli = models.CharField(max_length=6, choices=gender_choices)
	katisyys = models.CharField(max_length=28, choices=hands_choices)
	nykyinen_asuinpaikka = models.CharField(max_length=1000, default="nowhere")
	aidinkieli = models.CharField(max_length=1000, default="none")
	muut_kielet = models.CharField(max_length=1000, default="no")
	kielia_kaytat = models.CharField(max_length=1000, default="neither")
	korkein_tutkinto = models.CharField(max_length=26, choices=education_choices)
	paaaine_ala = models.CharField(max_length=1000, default="none")
	jos_opiskelija_tutkintoa  = models.CharField(max_length=26, choices=degree_choices)
	lukihairio = models.CharField(max_length=5, choices=yes_no)
	kuulonalenema = models.CharField(max_length=5, choices=yes_no)
	kommentteja = models.TextField(default='nothing')

class feedback(models.Model):
	str_disagree ='VahvastiEriMielta'
	disagree ='EriMielta'
	neither ='EiSamaaEikaEriMielta'
	agree ='SamaaMielta'
	str_disagree ='VahvastiSamaaMielta'	
	opinion_choices = (
		(str_disagree, 'Vahvasti eri mieltä'),
		(disagree, 'Eri mieltä'),
		(neither, 'Ei samaa eikä eri mieltä'),
		(agree, 'Samaa mieltä'),
		(str_disagree, 'Vahvasti samaa mieltä'),	
		)
	bad ='Huono'
	ok ='Kohtalainen'
	good ='Hyva'
	vgood ='TodellaHyva'
	performance_choices = (
		(bad, 'Huono'),
		(ok, 'Kohtalainen'),
		(good, 'Hyvä'),
		(vgood, 'Todella hyvä'),
		)
	all_the_time = 'KokoAjan'
	most_of_the_time = 'SuurimmanOsanAjasta'
	some_time = 'JonkinVerranAjasta'
	very_little_time = 'HyvinVahanAjasta'
	not_at_all = 'EhYhtaan'
	understanding_choices = (
		(all_the_time, 'Koko ajan'),
		(most_of_the_time, 'Suurimman osan ajasta'),
		(some_time, 'Jonkin verran ajasta'),
		(very_little_time, 'Hyvin vähän ajasta'),
		(not_at_all, 'En yhtään'),
		)
	session_key = models.CharField(max_length=40)
	ohjeet = models.CharField(max_length=25, choices=opinion_choices)
	mita_tein = models.CharField(max_length=25, choices=opinion_choices)
	yksinkertainen = models.CharField(max_length=25, choices=opinion_choices)
	vaativa = models.CharField(max_length=25, choices=opinion_choices)
	paineita = models.CharField(max_length=25, choices=opinion_choices)
	hauskaa = models.CharField(max_length=25, choices=opinion_choices)
	heijastaa = models.CharField(max_length=25, choices=opinion_choices)
	suoritustasi = models.CharField(max_length=25, choices=performance_choices)
	ymmarsin = models.CharField(max_length=25, choices=understanding_choices)
	tehtava = models.TextField(default='nothing')
	strategian = models.TextField(default='nothing')
	kriteereita = models.TextField(default='nothing')
	vaikutelman = models.TextField(default='nothing')
	kommentteja = models.TextField(default='nothing') 


class test(models.Model):
	session_key = models.CharField(max_length=40)
	checkbox = models.TextField(default='nothing')
	index = models.IntegerField()
	question = models.CharField(max_length=10)

class sessions(models.Model):
	session_id = models.CharField(max_length=40)
	session_key = models.TextField(default='nothing')
	ip = models.CharField(max_length=400)
	published_date = models.DateTimeField(blank=True, null=True)
