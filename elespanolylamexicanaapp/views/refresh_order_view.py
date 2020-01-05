from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from elespanolylamexicanaapp.models.order import Order

class RefreshOrderServiceView(View):
    def get(self, request):
        
        dResponse = { 'thereOrders': False }        
        qFilter = Q( typeDelivery=Order.PENDING )        
        oOrders = Order.objects.filter( qFilter )
        
        if len( oOrders ) > 0:
            dResponse = { 'thereOrders': True }
        
        return JsonResponse(dResponse)