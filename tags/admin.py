from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    exclude = ('slug',)
    # prepopulated_fields = {'slug': ('name',)}