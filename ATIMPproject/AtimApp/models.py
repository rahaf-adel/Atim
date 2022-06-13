from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class University(models.Model):
    """A simple model that add university to the system"""
    name = models.CharField(max_length=40)
    description = models.TextField()
    city = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(models.Model):
    """A simple model that company university to the system"""
    name = models.CharField(max_length=40)
    description = models.TextField()
    city = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Graduete_Students(models.Model):
    """A simple model that add student information to the system"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    major = models.CharField(max_length=50)
    GPA = models.DecimalField(decimal_places=2, max_digits=3)
    graduete_date = models.DateField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Job_Offer(models.Model):
    """A simple model that add job offer to the system"""
    name = models.CharField(max_length=40)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    student = models.ForeignKey(Graduete_Students, on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=None, null=True)

    def __str__(self):
        return self.name
