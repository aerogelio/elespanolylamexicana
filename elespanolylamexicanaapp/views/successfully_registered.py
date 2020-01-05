from django.views import View
from django.shortcuts import render, redirect

class SuccessfullyRegisteredView( View ):
    
    def get(self, request):
        
        if request.user.is_active and not request.user.is_authenticated:
            return redirect( 'home' )
        
        return render( request, 'elespanolylamexicanaapp/successfully_registered.html' )