
from django.db import models
from django.contrib.auth.models import User

class SportsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class SportsEvent(models.Model):
    category = models.ForeignKey(SportsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
