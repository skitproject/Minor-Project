from django.contrib import admin
from .models import post


class postModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'contant']

    class Meta:
        model = post


admin.site.register(post, postModelAdmin)
