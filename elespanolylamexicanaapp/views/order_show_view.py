from django.views import View
from django.shortcuts import render
from elespanolylamexicanaapp.utils.utils import sum_total
from elespanolylamexicanaapp.models.order import Order

class OrderShowView( View ):
    
    def get( self, request, order_id ):
        oOrder = Order.objects.get(pk=order_id)
        
        oOrder.total = sum_total([oOrder.tax, oOrder.subtotal])
        
        return render( request, 'elespanolylamexicanaapp/order_show.html', { 'oOrder': oOrder } )