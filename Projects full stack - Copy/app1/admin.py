from django.contrib import admin

# Register your models here.
from app1.models import productsinput, cartitems, Orderdetails, Orderitems, Reviews

admin.site.register(productsinput)
admin.site.register(cartitems)
admin.site.register(Orderdetails)
admin.site.register(Orderitems)
admin.site.register(Reviews)


