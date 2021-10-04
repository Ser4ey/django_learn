from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    fields = ('title', 'content', 'photo', 'get_photo', 'is_published',
              'category', 'created_at', 'updated_at', 'views')
    readonly_fields = ('created_at', 'updated_at', 'get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    get_photo.short_description = 'Миниатюра'


    # поля которые можно редактировать не заходя в режим редактирование
    list_editable = ('is_published',)

    # поля по которым можно фильтровать
    list_filter = ('category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)




