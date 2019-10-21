from django.db import models
from django.conf import settings

# Create your models here.

class Dcinside(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Comment(models.Model):
    dcinside = models.ForeignKey(Dcinside, on_delete=models.CASCADE)
    reply = models.CharField(max_length=100)
    c_created_at = models.DateTimeField(auto_now_add=True)
    c_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    