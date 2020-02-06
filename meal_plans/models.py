from django.db import models

# Create your models here.
class Topic (models.Model):
    title = models.CharField (max_length=220)
    date = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.title 

class Entry (models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    entry = models.TextField ()
    date_added = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__ (self):
        return self.entry [:50] + "..."