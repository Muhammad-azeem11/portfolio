from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
