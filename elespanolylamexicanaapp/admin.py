from django.contrib import admin

# Register your models here.
from .models.product import Product
from .models.tax import Tax
from .models.category import Category
from .models.order import Order

def total( obj ):
    return obj.subtotal + obj.tax

def cambiar_status_a_CANCELADA( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.CANCEL )
    
def cambiar_status_a_PENDING( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.PENDING )
    
def cambiar_status_a_ACEPTADA( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.ACCEPTED )
    
def cambiar_status_a_PREPARANDOSE( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.PREPARING )
    
def cambiar_status_a_RECOGER( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.PICK_UP )
    
def cambiar_status_a_ENTREGADA( modeladmin, request, queryset ):
    queryset.update( typeDelivery=Order.DELIVERED )
    
class OrderAdmin( admin.ModelAdmin ):
    class Media:
        js = ("js/refresh-order.js",)
    
    list_display = [ 'user', 'typeDelivery', 'subtotal', 'tax', total, 'description' ]
    actions = [cambiar_status_a_CANCELADA, cambiar_status_a_PENDING, cambiar_status_a_ACEPTADA, cambiar_status_a_PREPARANDOSE,
               cambiar_status_a_RECOGER, cambiar_status_a_ENTREGADA]

admin.site.disable_action('delete_selected')
#admin.site.add_action( change_status_to_done, 'Cambiar status a PEDIDO LISTO' )


admin.site.register( Product )
admin.site.register( Tax )
admin.site.register( Category )
admin.site.register( Order, OrderAdmin )