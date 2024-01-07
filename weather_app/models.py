from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100) # city name

    def __str__(self):
        return self.name