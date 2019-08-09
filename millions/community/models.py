from django.db import models
from users.models import User

#게시물
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="title", max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(verbose_name="body")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return '%s - %s' % (self.id, self.title)

    def summary(self):
        return self.body[:100]

#댓글
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(verbose_name="body")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-updated']
    
    def __str__(self):
        return self.id      #수정 예정

    def summary(self):
        return self.body[:100]
    

