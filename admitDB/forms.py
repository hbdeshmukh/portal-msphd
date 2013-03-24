from django import forms

class studentRegisterForm(forms.Form):
    first_name = forms.CharField(label=(u'First Name'))
    last_name = forms.CharField(label=(u'Last Name'))
    BITS_ID = forms.CharField(label=(u'BITS ID'))
    email = forms.EmailField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))

class studentInfoForm(forms.Form):
    discipline = forms.CharField(label=(u'Discipline Code'))#dictionary object for code to name matching of discipline
    target_discipline = forms.CharField(label=(u'Discipline for Graduate Studies'))
    sub_area = forms.CharField(label=(u'Area of Specialization'))
    cgpa = forms.FloatField(label=(u'CGPA'))
    gre_verbal = forms.IntegerField(label=(u'Verbal score'))
    gre_quant = forms.IntegerField(label=(u'Quant score'))
    gre_essay = forms.FloatField(label=(u'Essay score'))
    toefl_total = forms.IntegerField(label=(u'TOEFL total score'))
    toefl_speaking = forms.IntegerField(label=(u'TOEFL speaking score'))