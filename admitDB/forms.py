from django import forms

class studentForm(forms.Form):
	name = forms.CharField(label=(u'Name'))
	BITS_ID = forms.CharField(label=(u'BITS ID'))
	email = forms.EmailField(label=(u'Email'))
	password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))

