from django.conf import settings
from django.db import models
from users.models import CustomUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "book"
        ordering = ['title']
    
    def __str__(self):
        # return f"{self.title} by {self.author} (Genre: {self.genre})"
        return f"{self.title} - {self.author} - {self.genre}"
