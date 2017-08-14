import os
from django.contrib import admin

# Register your models here.
from Auto_test.models import Appconfig, Column


class AppconfigInline(admin.TabularInline):
    model = Appconfig
    extra = 1 #默认行

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name','platform','slug','intro','update_time')  # list
    search_fields = ('name','status','platform', 'slug','intro')
    inlines = [AppconfigInline]  # Inline 内联
    #actions = ['make_story_public']

    # def make_story_public(self, request, queryset):
    #     # queryset参数为选中的Story对象
    #     rows_updated = queryset.update(status=2)
    #     message_bit = "%s 项目" % rows_updated
    #     self.message_user(request, "%s 项目已执行测试" % message_bit)
    #
    # make_story_public.short_description = u'执行测试=>所选项目 '

class TestpageAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')  # list
    search_fields = ('name', 'intro')


class TestcaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'element','pub_date')  # list
    search_fields = ('name', 'element','content')

admin.site.register(Column, ColumnAdmin)
#admin.site.register(Testpage, TestpageAdmin)
#admin.site.register(Testcase, TestcaseAdmin)