from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title