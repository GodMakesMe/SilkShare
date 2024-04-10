from django.shortcuts import render
from .models import Profile, Post, Friend, Notification, Group, Settings, Message, PostLike, Comment, Follow, Report, Block

def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def friend_detail(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    return render(request, 'friend_detail.html', {'friend': friend})

def notification_detail(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    return render(request, 'notification_detail.html', {'notification': notification})

def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'group_detail.html', {'group': group})

def settings_detail(request, settings_id):
    settings = Settings.objects.get(id=settings_id)
    return render(request, 'settings_detail.html', {'settings': settings})

def message_detail(request, message_id):
    message = Message.objects.get(id=message_id)
    return render(request, 'message_detail.html', {'message': message})

def postlike_detail(request, postlike_id):
    postlike = PostLike.objects.get(id=postlike_id)
    return render(request, 'postlike_detail.html', {'postlike': postlike})

def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'comment_detail.html', {'comment': comment})

def follow_detail(request, follow_id):
    follow = Follow.objects.get(id=follow_id)
    return render(request, 'follow_detail.html', {'follow': follow})

def report_detail(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'report_detail.html', {'report': report})

def block_detail(request, block_id):
    block = Block.objects.get(id=block_id)
    return render(request, 'block_detail.html', {'block': block})

