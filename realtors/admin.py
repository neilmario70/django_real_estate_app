from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    # list_editable = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Realtor, RealtorAdmin)