from django import forms
from .models import background, feedback
 
class checkboxfield(forms.Form):
	check_box = forms.BooleanField(required=False)


class backgroundForm(forms.ModelForm):
	yes_no = (
		('Yes', 'Kyllä'),
		('No', 'Ei'),
		)
	degree = forms.CharField(required=False)
	other_languages = forms.CharField(required=False)
	comments = forms.CharField(widget=forms.Textarea, required=False)
	dyslexia = forms.CharField(widget=forms.RadioSelect(choices=yes_no))
	hearing = forms.CharField(widget=forms.RadioSelect(choices=yes_no))

	class Meta:
		model = background
		fields = ('age', 'sex', 'hand', 'place', 'language', 'other_languages',\
		 'used_language', 'education', 'major', 'degree', 'dyslexia', 'hearing', 'comments',)

class feedbackForm(forms.ModelForm):
	instructions = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	doing = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	simple = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	demanding = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	pressure = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	fun = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	reflects = forms.CharField(widget=forms.RadioSelect(choices=feedback.opinion_choices))
	performance = forms.CharField(widget=forms.RadioSelect(choices=feedback.performance_choices))
	understanding = forms.CharField(widget=forms.RadioSelect(choices=feedback.understanding_choices))	
	task = forms.CharField(widget=forms.Textarea, required=False)
	strategy = forms.CharField(widget=forms.Textarea, required=False)
	criteria = forms.CharField(widget=forms.Textarea, required=False)
	impression = forms.CharField(widget=forms.Textarea, required=False)
	comments = forms.CharField(widget=forms.Textarea, required=False)
	class Meta:
		model = feedback
		fields = ('instructions', 'doing', 'simple', 'demanding', 'pressure',\
			'fun', 'reflects', 'performance', 'understanding', 'task', 'strategy',\
			 'criteria', 'impression', 'comments',)
	
