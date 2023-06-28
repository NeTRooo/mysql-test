from django.contrib import admin
from .models import BuyStatus, PrimeStatus

#  
#  configuring the display
#  

# user, nick, access, prime, pay
class BuyStatusAdmin(admin.ModelAdmin):
    list_display = ('nick', 'access', 'pay')
    list_display_links = ('nick', 'access')
    search_fields = ('nick', 'access')
    list_editable = ('pay',)
    list_filter = ('pay',)

# user email nick pay_id start_date end_date
class PrimeStatusAdmin(admin.ModelAdmin):
    list_display = ('nick', 'start_date', 'end_date')
    list_display_links = ('nick', 'start_date', 'end_date')
    search_fields = ('nick', 'start_date', 'end_date', 'pay_id')

#  
#  Register model
#  

admin.site.register(PrimeStatus, PrimeStatusAdmin)
admin.site.register(BuyStatus, BuyStatusAdmin)