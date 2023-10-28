from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title = "پنل "
admin.sites.AdminSite.index_title = "پنل مدیریت "


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', 'author', ('publish', JDateFieldListFilter)]
    search_fields = ['title', 'description']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug": ['title']}

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone']
