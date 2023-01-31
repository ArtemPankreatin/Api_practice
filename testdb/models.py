from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        user = "user",
        admin = "admin"
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.user)
    list_of_favorite_books = ArrayField(base_field=models.CharField(max_length=6) )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Book(AbstractBaseUser):
    name = models.CharField(max_length=50, unique=True)
    id_author = models.IntegerField()
    id_genre = models.IntegerField()
    date_of_issue = models.DateField()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []


class Author(AbstractBaseUser):
    name = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

class Genre(AbstractBaseUser):
    name = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
