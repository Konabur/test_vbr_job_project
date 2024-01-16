from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Обязательное поле для хранения пароля

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @staticmethod
    def create_user(email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = email.lower()
        user = User(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class Organization(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    members = models.ManyToManyField(User, related_name='organizations', blank=True)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization, related_name='events')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateTimeField()
