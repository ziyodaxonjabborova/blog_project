from django.db import models

class Post(models.Model):
    image=models.FileField(upload_to="images")
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    desc=models.TextField()
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
