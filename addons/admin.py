from django.contrib import admin
from .models import Whitelist

#  
#  configuring the display
#  

# name
class WhitelistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

# user email nick pay_id start_date end_date
# class PrimeStatusAdmin(admin.ModelAdmin):
#     list_display = ('nick', 'start_date', 'end_date')
#     list_display_links = ('nick', 'start_date', 'end_date')
#     search_fields = ('nick', 'start_date', 'end_date', 'pay_id')

#  
#  Register model
#  

admin.site.register(Whitelist, WhitelistAdmin)
# admin.site.register(BuyStatus, BuyStatusAdmin)