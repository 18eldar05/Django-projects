from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class EstiemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_create', 'get_html_photo', 'is_published', 'kind')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'kind', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=75>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class KindAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Estiem, EstiemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Kind, KindAdmin)

admin.site.index_title = 'Админ-панель'
admin.site.site_title = 'ESTIEM администрирование'
admin.site.site_header = mark_safe("<img class='logo' src=\"/media/photos/estiem_logo.png\"><span class='logo_text'>администрирование</span>")
