from django.views import View
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth import login
from elespanolylamexicanaapp.forms.user_app_form import UserappForm
from elespanolylamexicanaapp.forms.user_form import UserForm

class SignInView(View):
    
    def get(self, request, ):
        
        userappForm = UserappForm(  )
        userForm = UserForm(  )
        
        return render( request, 'elespanolylamexicanaapp/signin.html', { 'userappForm': userappForm, 'userForm':userForm } )
    
    @transaction.atomic
    def post(self, request, ):
        
        userForm = UserForm( request.POST )
        userappForm = UserappForm( request.POST )
        
        if userForm.is_valid() and userappForm.is_valid():
            userForm.is_active = 0
            
            oUser = userForm.save()
            oUserapp = userappForm.instance
            oUserapp.user = oUser
            oUserapp.save()
            
            login( request, oUser )
            
            return redirect( 'successfully-registered' )
            
        return render( request, 'elespanolylamexicanaapp/signin.html', { 'userappForm': userappForm, 'userForm': userForm } )