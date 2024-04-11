from django.db import models

class Topic(models.Model):
    '''A topic that user is learning'''
    text=models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    '''Something specified learned about a topic'''

    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= "entries"

    def __str__(self):
        t=self.text
        if len(t)>50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
        
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title