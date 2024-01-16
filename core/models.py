from django.db import models


class User(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Обязательное поле для хранения пароля


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
