from django.contrib import admin
from .models import *

from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title ="پنل مدیریت"
admin.sites.AdminSite.index_title = "داشبورد"
# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', ('publish', JDateFieldListFilter), 'author']
    search_fields = ['title', 'description']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug": ['title']}
    list_editable = ['status']