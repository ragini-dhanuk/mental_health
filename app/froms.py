from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)