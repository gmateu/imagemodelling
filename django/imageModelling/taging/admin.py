# -*- coding: utf-8 -*-
from imageModelling.taging.models import Tag,Picture
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class PictureAdmin(admin.ModelAdmin):
    fields = ['caption','image']

admin.site.register(Tag, TagAdmin)
admin.site.register(Picture,PictureAdmin)

