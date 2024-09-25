from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug', 'img_preview','price']
   
    readonly_fields = ['img_preview']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug',]
   
admin.site.register(Category,CategoryAdmin)

admin.site.register(Profile)
admin.site.register(CartItem)
admin.site.register(OrderStatus)
admin.site.register(PaymentType)    
admin.site.register(Order)
admin.site.register(Orderproduct)

