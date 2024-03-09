from django import forms

from app.models import *



class userform(forms.Form):

    sname = forms.CharField(max_length=100)
    age =  forms.IntegerField()





































class usermodelform(forms.ModelForm):

    class Meta:
        model = user

        fields = '__all__'

        
