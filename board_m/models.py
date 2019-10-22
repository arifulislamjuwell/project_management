from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    creater=models.ForeignKey(User, on_delete= models.CASCADE)
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    descrip=models.CharField(max_length=200)

    def __str__(self):
        return self.title