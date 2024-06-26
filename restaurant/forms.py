from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for dishes', max_length=255)
