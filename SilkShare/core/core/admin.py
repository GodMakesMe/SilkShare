from django.contrib import admin
from .models import Profile, Post, Friend, Notification, Group, Settings, Message, PostLike, Comment, Follow, Report, Block

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Notification)
admin.site.register(Group)
admin.site.register(Settings)
admin.site.register(Message)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Report)
admin.site.register(Block)