from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registration(models.Model):
	user = models.OneToOneField(User, related_name='user_profile')
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
			return self.firstname
	