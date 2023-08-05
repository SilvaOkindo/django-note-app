from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class User(AbstractBaseUser):
#     profile_pic = models.ImageField(upload_to="profile-pics")
#     email = models.EmailField()
#     password = models.CharField()
#

# class User(AbstractBaseUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)
#
#     # profile_pic = models.ImageField(upload_to='profile-pictures')
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
