from django.contrib import admin

from .models import Profile, Post, Friend, Notification, Group, Settings

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Notification)
admin.site.register(Group)
admin.site.register(Settings)
