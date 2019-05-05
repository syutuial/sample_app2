from django.db import models


class Task(models.Model):
    name = models.CharField('taskname', max_length=255)
    created_date = models.DateTimeField('createddate', auto_now_add=True)
    update_date = models.DateTimeField('updatedate', auto_now=True)

    def __str__(self):
        return self.name
