from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post,Comment,Category

class PostAdmin(SummernoteModelAdmin):
    list_display=['title','publis_date','draft']
    list_filter=['draft']
    search_fields=['title','content']

    summernote_fields = ('content',)


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)

