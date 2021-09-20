from django.contrib import admin

# Register your models here.
from.models import Student,Techer


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','marks','city','pass_date']


@admin.register(Techer)
class TecherAdmin(admin.ModelAdmin):
    list_display = ['id','name','empnum','city','salary','join_date']