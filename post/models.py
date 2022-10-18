from django.db import models

#from users.models import User

class Comment(models.Model):
    content = models.CharField(max_length=80)
    create_date = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.content)

