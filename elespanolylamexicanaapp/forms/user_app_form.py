from django import forms
from elespanolylamexicanaapp.models.user_app import Userapp

class UserappForm( forms.ModelForm ):

    class Meta:
        model = Userapp
        exclude = ('user',)