from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50) 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institute}"