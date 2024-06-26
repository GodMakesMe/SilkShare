from django.shortcuts import render
from learning_logs.models import Topic, Entry


def index(request):
    '''The home page for learning log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Show all topics'''
    topics=Topic.objects.order_by('date_added')
    
    context= {'topics':topics}

    return render(request, 'learning_logs/topics.html', context)