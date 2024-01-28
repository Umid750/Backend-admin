from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'picture', 'post_category', 'post_date',)
    list_filter = ['post_date',]
    def picture(self, rasm):
        return mark_safe(f"<img src = '{rasm.post_image}' width = '250' />")

admin.site.register(Post, PostAdmin)
admin.site.register(Category)