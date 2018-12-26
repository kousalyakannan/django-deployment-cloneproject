from django import forms
from youtubeapp.models import Search

class SearchForm(forms.ModelForm):
    
    class Meta():
        model = Search
        fields = ('title',)



