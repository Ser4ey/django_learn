from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

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




