import decimal
from elespanolylamexicanaapp.models.product import Product

def sum_total( list_elements ):
    #realizar calculos precisos
    total = decimal.Decimal(0.00)
    for element in list_elements:
        total += decimal.Decimal( element )
    
    return round(total, 2)

def get_subtotals( lpkProducts ):
    subtotal = decimal.Decimal( '0.00' )
    iva = decimal.Decimal('0.00')
    total = decimal.Decimal('0.00')
    
    #Si hay ids repetidos solo regresa 1 objeto y no todos.
    #loProducts = Product.objects.filter( id__in=lpkProducts )
    for pkProduct in lpkProducts:
        oProduct = Product.objects.get( pk=pkProduct )
        subtotal += decimal.Decimal( str( oProduct.price ) )
        for tax in oProduct.taxes.all():
            iva += (oProduct.price * (tax.percentage/decimal.Decimal('100')))
    
    total = subtotal + iva    
    
    return {'subtotal': str(round(subtotal,2)), 'tax': str(round(iva,2)), 'total': str(round(total,2))}