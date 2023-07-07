from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class SubCategory(models.Model):
    category_id = models.ForeignKey(Category , blank=False , null=False , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    

class Product(models.Model):
    name = models.CharField(max_length=255 , blank=False, null=False , unique=True)
    quantity_per_pack = models.IntegerField( blank=True, null=True)
    quantity_per_unit = models.IntegerField( blank=True, null=True)
    price_per_quantity = models.IntegerField()
    price_per_unit = models.IntegerField()
    '''content_type = models.ForeignKey(ContentType,
                                     limit_choices_to= {'model__in':(
                                        'Category' , 'SubCategory')}, 
                               on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')'''
    
    def __str__(self):
        return self.name
    
    @classmethod
    def all_columns(cls):
        return [f.get_attname() for f in Product._meta.fields]


class Purchase(models.Model):
    product = models.ForeignKey(Product , on_delete=models.DO_NOTHING)
    quantity_per_pack = models.IntegerField(blank= True , null=False)
    quantity_per_unit = models.IntegerField(blank=True, null=False)
    price = models.IntegerField()
    date_purchased = models.DateTimeField(auto_now_add=True)
    
    
    @classmethod
    def all_columns(cls):
        return [f.get_attname() for f in Purchase._meta.fields]
    
    def __str__(self):
        if self.restock is True:
            return 'Bought' + ' ' + self.product.name
        else:
            return 'Sold' + ' ' + self.product.name
    
    def check_restock(self):
        message = _("Restock has to purchased by someone ")
        if self.restock is True and self.purchased is None:
            raise ValidationError({'restock' : message ,
                                   'purchased_by': message})
    
    def clean(self):
        
        if self.quantity_per_pack is None and self.quantity_per_unit is None:
            raise ValidationError(_("Quantity Per Pack and Quantity per Unit can't be empty "))
        else: 
            if self.quantity_per_pack is None:
                self.quantity_per_pack = 0
            if self.quantity_per_unit is None:
                self.quantity_per_unit = 0
            if self.change_given is None:
                self.change_given = 0
                
        self.check_restock()
                
        self.price = self.product_price
        
    def product_price(self):
        return self.quantity_per_pack * self.product.price_per_quantity + self.quantity_per_unit * self.product.price_per_unit
    
    
class Order(models.Model):
    purchases = models.ManyToManyField(Purchase, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    purchased_by = models.CharField(max_length = 255, blank=True, null=False)
    paid = models.BooleanField(default = True , blank=False , null=False)
    amount_paid = models.IntegerField()
    change_given = models.IntegerField(blank = True , null=False)
    restock = models.BooleanField(default=False)

    
class CashInventory(models.Model):
    cash_at_hand = models.IntegerField()
    expenditure = models.IntegerField()
    revenue = models.IntegerField()
