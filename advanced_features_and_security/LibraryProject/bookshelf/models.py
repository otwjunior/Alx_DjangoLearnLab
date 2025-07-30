from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class  Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100) 
    publication_year = models.IntegerField()

stomizing user authentication
class UserManager(BaseUserManager):  #manages the db queries for user model
    def create_user(self, username, password=None, date_of_birth=None, profile_photo=None):
        """ create a user with  username, password, dob and profile photo"""
        if not  username:
            raise ValueError("username must be set")
        
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password) # ensure password is hashed
        user.save(using=self._db) # save user instance

        return user

    def create_superuser(self, username, password=None, date_of_birth=None, profile_photo=None):
        
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False, blank=False)
    profile_photo =models.ImageField(upload_to='images/')

    REQUIRED_FIELDS = ['password', 'date_of_birth', 'profile_photo']
    
    objects = UserManager()


