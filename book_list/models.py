from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} - {self.author}"