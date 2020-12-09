from django import forms
from .models import background, feedback
 
class checkboxfield(forms.Form):
	check_box = forms.BooleanField(required=False)


class backgroundForm(forms.ModelForm):
	yes = 'Kylla'
	no = 'Ei'
	yes_no = (
		(yes, 'Kyllä'),
		(no, 'Ei'),
		)
	jos_opiskelija_tutkintoa = forms.CharField(required=False, widget=forms.Select(choices=background.degree_choices))
	muut_kielet = forms.CharField(required=False)
	kommentteja = forms.CharField(widget=forms.Textarea(), required=False)
	lukihairio = forms.CharField(widget=forms.RadioSelect(choices=yes_no))
	kuulonalenema = forms.CharField(widget=forms.RadioSelect(choices=yes_no))

	class Meta:
		model = background
		fields = ('ika', 'sukupuoli', 'katisyys', 'nykyinen_asuinpaikka', 'aidinkieli', 'muut_kielet',\
		 'kielia_kaytat', 'korkein_tutkinto', 'paaaine_ala', 'jos_opiskelija_tutkintoa', 'lukihairio', 'kuulonalenema', 'kommentteja',)

class feedbackForm(forms.ModelForm):
	ohjeet = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	mita_tein = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	yksinkertainen = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	vaativa = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	paineita = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	hauskaa = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	heijastaa = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	suoritustasi = forms.CharField(widget=forms.RadioSelect(choices=feedback.performance_choices))
	ymmarsin = forms.CharField(widget=forms.RadioSelect(choices=feedback.understanding_choices))	
	tehtava = forms.CharField(widget=forms.Textarea(), required=False)
	strategian = forms.CharField(widget=forms.Textarea(), required=False)
	kriteereita = forms.CharField(widget=forms.Textarea(), required=False)
	vaikutelman = forms.CharField(widget=forms.Textarea(), required=False)
	kommentteja = forms.CharField(widget=forms.Textarea(), required=False)
	class Meta:
		model = feedback
		fields = ('ohjeet', 'mita_tein', 'yksinkertainen', 'vaativa', 'paineita',\
			'hauskaa', 'heijastaa', 'suoritustasi', 'ymmarsin', 'tehtava', 'strategian',\
			 'kriteereita', 'vaikutelman', 'kommentteja',)
