from django.db import models

# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=255)

class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя ')
    email = models.EmailField(verbose_name='Почта ')
    text = models.TextField(verbose_name='Сообщение ')

class Project(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    image = models.TextField()
    link = models.ImageField(upload_to='static')

class Biography(models.Model):
    title = models.CharField(max_length=300)
    discription = models.TextField()

class Secsub(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()

class Contact(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()

class Home(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()