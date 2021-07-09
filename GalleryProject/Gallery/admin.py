from django.contrib import admin

from .models import Image
# Register your models here.
@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','date']

# admin.site.register(Image)