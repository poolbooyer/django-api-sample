from django.db import models

# Create your models here.
class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField()

    class Meta:
        ordering = ['created']
