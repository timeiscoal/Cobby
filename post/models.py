from django.db import models
from user.models import User
from makgeolli.models import Makgeolli


class Comment(models.Model):
    content = models.CharField(max_length=80)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Makgeolli, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.content)
