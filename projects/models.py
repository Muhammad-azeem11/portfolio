from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title