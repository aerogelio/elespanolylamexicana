# -*- coding: utf-8 -*-
import decimal

from django.views import View
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from elespanolylamexicanaapp.models.product import Product
from elespanolylamexicanaapp.models.category import Category
from elespanolylamexicanaapp.models.order import Order
from elespanolylamexicanaapp.utils.utils import sum_total

class DashboardView( View ):
    
    @method_decorator( login_required )
    def get(self, request):
        
        #Update price menubar
        orderFilter = Q(userapp=request.user.userapp)
        #orderFilter.add(~Q( typeDelivery=Order.DELIVERED ), Q.AND)
        loOrders = Order.objects.filter( orderFilter ).order_by('-id')[:5]
        
        dOrder = { 'products': [], 'totals': [], 'total': 0.00, 'subtotals': {}}
        if request.session.get( 'order', False ):
            dOrder = request.session.get( 'order' )
        else:
            request.session[ 'order' ] = dOrder
            
        request.session.modified = True
        
        #start
        loCategories = Category.objects.all()
        queryFilter = Q()
        
        for paramCategory in request.GET:
            queryFilter.add( Q( category__name=paramCategory ), Q.OR )
            
        oProducts = Product.objects.filter( queryFilter )
            
        return render( request, 'elespanolylamexicanaapp/dashboard.html', { 'oProducts': oProducts,
                                                                            'dOrder': dOrder,
                                                                            'loCategories': loCategories,
                                                                            'lQParameters': request.GET,
                                                                            'loOrders': loOrders,
                                                                            } )
    
    def post( self, request ):
        
        loCategories = Category.objects.all()
        oProducts = Product.objects.all()
        pkProduct = request.POST['pk']
        dOrder = { 'products': [], 'totals': [], 'total': 0.00, 'subtotals': {} }
        oProduct = Product.objects.get( pk=pkProduct )
        
        orderFilter = Q(userapp=request.user.userapp)
        #orderFilter.add(~Q( typeDelivery=Order.DELIVERED ), Q.AND)
        loOrders = Order.objects.filter( orderFilter ).order_by('-id')[:5]
        
        if oProduct is not None:
            if request.session.get( 'order', False ):
                dOrder = request.session.get( 'order' )
                dOrder['products'].append( oProduct.pk )
                dOrder['totals'].append( float(oProduct.total()) )
            else:
                request.session[ 'order' ] = dOrder
                dOrder['products'].append( pkProduct )
            
            request.session.modified = True
                
            dOrder['total'] = float(sum_total( dOrder['totals'] ))        
        return render( request, 'elespanolylamexicanaapp/dashboard.html', { 'oProducts': oProducts,
                                                                           'dOrder': dOrder,
                                                                           'loCategories': loCategories,
                                                                           'loOrders': loOrders} )