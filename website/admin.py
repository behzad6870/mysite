from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display=['name','subject','email','created_date']
    list_filter=['email']
    search_fields=('message',)
admin.site.register(Contact,ContactAdmin)

# Register your models here.
