from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, UserManager, AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
	age = models.IntegerField(default=23)
	sex= models.CharField(max_length=10, default='Female')
	
	def __str__(self):
				 return str(self.email)

class Task(models.Model):
    name = models.TextField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.name
        else:
            return self.name
    def get_absolute_url(self):
        return reverse('list')
