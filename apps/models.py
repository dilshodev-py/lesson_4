from django.db import models
from django.db.models import Model, CharField, IntegerField, DateField


class Task(Model):
    name = CharField(max_length=100)
    progress = IntegerField()
    due_date = DateField()

    def __str__(self):
        return self.name
