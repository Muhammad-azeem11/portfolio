from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    about = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
