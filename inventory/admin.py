from django.contrib import admin
from .models import Product , Purchase, CashInventory

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'quantity_per_pack' , 'quantity_per_unit' ,'price_per_quantity'
                    , 'price_per_unit' , 'category']
    list_filter = ('price_per_unit', 'category')
    
    
    
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product' , 'price'] 
    readonly_fields = ['product_price']
    list_filter = ['product']


# Register your models here.

admin.site.register(Product , ProductAdmin)
admin.site.register(Purchase , PurchaseAdmin)
admin.site.register(CashInventory)