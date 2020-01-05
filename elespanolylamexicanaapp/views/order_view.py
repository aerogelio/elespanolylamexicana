import decimal
from django.views import View
from django.db import transaction
from django.shortcuts import render, redirect
from elespanolylamexicanaapp.utils.utils import sum_total, get_subtotals
from elespanolylamexicanaapp.models.product import Product
from elespanolylamexicanaapp.models.order import Order, OrderProduct

class OrderView(View):
    
    def get( self, request ):       
        
        loProducts = []
        
        #Update price menubar
        dOrder = { 'products': [], 'totals': [], 'total': 0.00, 'subtotals': {} }
        if request.session.get( 'order', False ):
            dOrder = request.session.get( 'order' )
            request.session.modified = True
        else:
            request.session[ 'order' ] = dOrder
            request.session.modified = True
            
        for pkProduct in dOrder['products']:
            oProduct = Product.objects.get( pk=pkProduct )
            loProducts.append( oProduct )
            
        #Replace by object that do all
        dOrder['subtotals'] = get_subtotals( dOrder['products'] )
        
        return render( request, "elespanolylamexicanaapp/order.html", { 'dOrder': dOrder,
                                                                        'oProducts': loProducts } )
    
    
    def post(self, request):
        
        loProducts = []
        lsErrors = []
        #Update price menubar
        dOrder = { 'products': [], 'totals': [], 'total': 0.00, 'subtotals': {} }
        
        if request.session.get( 'order', False ):
            dOrder = request.session.get( 'order' )
            request.session.modified = True
        else:
            request.session[ 'order' ] = dOrder
            request.session.modified = True
        
        if request.POST['_method'] == 'POST':
            oOrder = Order()
            
            lpkProducts = dOrder['products']
            if len( lpkProducts ) > 0:
                oOrder.typeDelivery = Order.PENDING
                oOrder.subtotal = dOrder['subtotals']['subtotal']
                oOrder.tax = dOrder['subtotals']['tax']
                
                #try catch
                #atomic
                try:
                    with transaction.atomic():
                        oOrder.userapp = request.user.userapp
                        oOrder.save()
                        
                        for pkProduct in lpkProducts:
                            oProduct = Product.objects.get(pk = pkProduct)
                            oOrderProduct = OrderProduct()
                            oOrderProduct.order = oOrder
                            oOrderProduct.product = oProduct
                            oOrderProduct.save()
                        
                        del request.session['order']
                        request.session.modified = True
                except Exception as e:
                    print("ex")
                    print( e )
                
                return redirect('dashboard')
                    
            else:
                lsErrors.append( 'Agregue un producto al carrito.' )
        elif request.POST['_method'] == 'DELETE':
            pkProductToRemove = request.POST['pk']
            
            oProduct = Product.objects.get( pk=pkProductToRemove )
            dOrder['products'].remove( int(pkProductToRemove) )
            dOrder['totals'].remove( float( oProduct.total() ) )
            dOrder['total'] = float( sum_total( dOrder['totals'] ) )
            
            request.session['order'] = dOrder
            request.session.modified = True
            
            for pkProduct in dOrder['products']:
                oProduct = Product.objects.get( pk=pkProduct )
                loProducts.append( oProduct )
        
        dOrder['subtotals'] = str( get_subtotals( dOrder['products'] ) )
        
        return render( request, "elespanolylamexicanaapp/order.html", { 'dOrder': dOrder,
                                                                        'oProducts': loProducts,
                                                                        'lsErrors': lsErrors} )