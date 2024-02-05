from django.contrib import admin
from app.models import *
# Register your models here.

class CustomizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['email']
    list_editable=['name']
    list_filter=('url',)
    search_fields=['name']
admin.site.register(Topic)
admin.site.register(Webpage,CustomizeWebpage)
admin.site.register(AccessRecord)