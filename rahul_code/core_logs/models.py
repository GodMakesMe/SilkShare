from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rating  = models.IntegerField()
    interests = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        

class Post(models.Model):
    title = models.CharField(max_length=200)
    photos = models.ImageField(upload_to='photos/')
    videos = models.FileField(upload_to='videos/')  # Add this line to include videos field
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    tag = models.ManyToManyField(Tag)
#    link = models.URLField()  # Add this line to include link field
    def __str__(self):
        return self.title
    
class Friend(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_friend_requests')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('blocked', 'Blocked')])

    def __str__(self):
        return f"{self.sender.name} - {self.receiver.name}"

class Notification(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
    related_content = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.notification_type}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Profile)
    administrators = models.ManyToManyField(Profile, related_name='administered_groups')
    posts = models.ManyToManyField(Post)
#    comments = models.ManyToManyField(Comment)
#    interactions = models.ManyToManyField(Interaction)
#
    def __str__(self):
        return self.name
#    
class Settings(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    notification_settings = models.BooleanField(default=True)
    privacy_settings = models.BooleanField(default=False) # Anonimity is always false
#    theme_preferences = models.CharField(max_length=100)
#    language_preferences = models.CharField(max_length=100)
    password_change = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}'s settings"
#
#class Message(models.Model):
#    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
#    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
#    message_content = models.TextField()
#    timestamp = models.DateTimeField(auto_now_add=True)
#    read_status = models.BooleanField(default=False)
#
#class PostLike(models.Model):
#    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#class Comment(models.Model):
#    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)
#    comment_content = models.TextField()
#    timestamp = models.DateTimeField(auto_now_add=True)
#
#class Follow(models.Model):
#    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
#    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

class Report(models.Model):
    reporter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reported_content = models.TextField()
    reason = models.TextField()
#

#class Block(models.Model):
#    blocker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocking')
#    blocked = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocked_by')





# In a social website, backend variables typically represent the various pieces of information associated with users, posts, comments, likes, relationships between users, and other relevant data. Here's an overview of some common backend variables you might find in a social website:

# User Profile:

# Username
# Email
# Password (hashed for security)
# Profile picture/avatar
# Biography/About Me section
# Date of birth
# Location
# Privacy settings
# Activity status (online/offline)
# Account status (active, suspended, banned, etc.)

# Posts:

# Content/text of the post
# Author (reference to the user who posted it)
# Timestamp of when the post was created
# Number of likes
# Number of comments
# Privacy settings (public, private, friends only)
# Tags or categories
# Any attached media (photos, videos, links)

# Comments:

# Content/text of the comment
# Author (reference to the user who posted it)
# Timestamp of when the comment was created
# Post (reference to the post it belongs to)
# Number of likes
# Replies to the comment (if threaded comments are supported)

# Likes/Reactions:

# User who performed the like/reaction
# Post or comment that was liked/reacted to
# Type of reaction (like, love, laugh, etc.)
# Friendships/Connections:

# User who sent the friend request
# User who received the friend request
# Status of the friendship (pending, accepted, declined, blocked)

# Notifications:

# User receiving the notification
# Type of notification (new friend request, new message, post liked, etc.)
# Link to the related content (post, comment, user profile)

# Messages/Chats:

# Sender and receiver of the message
# Content/text of the message
# Timestamp of when the message was sent
# Status of the message (read, unread, deleted)
# Groups/Communities:

# Name of the group
# Description
# Members
# Group administrators/moderators
# Group posts, comments, and interactions
# Settings:

# Account settings (email preferences, notification settings, privacy settings)
# Theme preferences
# Language preferences
# Security settings (two-factor authentication, password change)
