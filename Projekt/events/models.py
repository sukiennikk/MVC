from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=200)
    is_confirmed = models.BooleanField(default=False, verbose_name="Obecność potwierdzona")

    def __str__(self):
        return self.name