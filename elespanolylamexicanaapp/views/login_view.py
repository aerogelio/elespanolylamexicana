# -*- coding: utf-8 -*-

from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class LogInView(View):
    
    def get( self, request ):
        if request.user.is_authenticated:
            return redirect( 'dashboard' )
        return render( request, 'elespanolylamexicanaapp/login.html' )
    
    def post(self, request):
        sError = None
        username = request.POST['username']
        password = request.POST['password']
        
        oUser = authenticate( request, username = username, password = password)
                
        if oUser is not None:
            login( request, oUser )
            return redirect( 'dashboard' )
        else:
            sError = 'El usuario o la contraseña es incorrecto.'
        
                
        return render( request, 'elespanolylamexicanaapp/login.html', { 'sError': sError } )
    