from django.db import models
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False, blank=True, null=True)
    due_date = models.DateField();
    objects = models.Manager()

    def __str__(self):
        return self.title
