'''Defines URL patterns for learning_logs'''

from django.urls import path

from .import views
app_name="learning_logs" #namespace

urlpatterns=[
    #Home Page
    path("", views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),

]
