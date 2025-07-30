from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    author =models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = [
            ("can_add_book", "canaddbook"),
            ("can_change_book", "canchangebook"),
            ("can_delete_book", "candeletebook"),
        ]
    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.name} has {self.book.title}"

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} serves at {self.library}"

# extend user model to create role based access
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member','Member'),
    ]

    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#creating the signal for userprofile creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


### customizing user authentication
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

