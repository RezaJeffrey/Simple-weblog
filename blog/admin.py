from django.contrib import admin
from .models import Article


class Blogadmin(admin.ModelAdmin):
    list_display = ('title','publisher','updated','status')
    list_filter = ('title','status','publisher','published')
    search_fields = ['title']
   
    list_editable = ('status','publisher')
    







admin.site.register(Article,Blogadmin)