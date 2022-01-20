from django.contrib import admin

# Register your models here.
from django. contrib import admin
from .models import Announcement
from .models import Rubric


class FriendAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'description', 'price', 'rubric')
    list_display_links = ('nick_name', 'description')
    search_fields = ('nick_name', 'description', )


admin.site.register(Announcement, FriendAdmin)
admin.site.register(Rubric)
