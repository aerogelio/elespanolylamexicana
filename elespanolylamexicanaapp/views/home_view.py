from django.views import View
from django.shortcuts import render

class HomeView(View):
    
    def get( self, request ):
        
        dOrder = { 'products': [], 'totals': [], 'total': 0.00 }
        if request.session.get( 'order', False ):
            dOrder = request.session.get( 'order' )
            request.session.modified = True
            
        return render( request, 'elespanolylamexicanaapp/home.html', { 'dOrder': dOrder } )