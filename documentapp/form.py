from django import forms

class PostForm(forms.Form):
    cClassName = forms.CharField(max_length=100, initial='')
    cClassDescription = forms.CharField(max_length=300, initial='')
    cClassOverview = forms.CharField(max_length=1000, initial='', required=False)
    cAuthor = forms.CharField(max_length=50, initial='')
    