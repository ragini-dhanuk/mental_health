from django import forms
from .models import Person

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('image','email','name','phone','address',
                  'city','state','pincode','education','mark_hs',
                  'mark_grad','resume','cover_letter',)