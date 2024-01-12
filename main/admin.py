from django.contrib import admin
from django.utils.html import format_html
from . models import Memory

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150" height="auto"/>')
    list_display = ['title', 'context', 'date', 'image']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ['date', 'updated', 'context']


