from django.contrib import admin

# Register your models here.
from enroll .models import Student

# class StudentAdmin(admin.ModelAdmin):
    
#     list_display = ('stuid','stuname')

# admin.site.register(Student,StudentAdmin)


@admin.register(Student)


class StudentAdmin(admin.ModelAdmin):


    list_display = ('stuid','stuname','stuemail')
    # list_editable = ['stuname','stuemail']
    list_display_links = ('stuname','stuemail',)
