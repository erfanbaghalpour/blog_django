from django.contrib import admin
from .models import *

admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title = "پنل "
admin.sites.AdminSite.index_title = "پنل مدیریت "

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', 'author', 'publish']
    search_fields = ['title', 'description']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug": ['title']}
