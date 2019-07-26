from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
)


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, gender=2, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username,
                          gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, 'blogs/like_section.html',  password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                                max_length=200, unique=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
        


    USERNAME_FILED = []
    REQUIRED_FILEDS = ['gender']

    def __str__(self):
        return self.username




