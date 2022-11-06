from django.db import models
from django.conf import settings

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='postings')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comment_list')
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.posting.title} - {self.content[:10]}...'
