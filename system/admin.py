from django.contrib import admin
from .models import Iha, Order, PrivateMsg

#IhaAdmin, OrderAdmin ve PrivateMsgAdmin modelleri burada oluşturuldu

class IhaAdmin(admin.ModelAdmin):
    list_display = ('iha_name', 'image', 'company_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('iha_name', 'date', 'to', 'employee_name')

class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(Iha, IhaAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)