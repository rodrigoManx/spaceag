import uuid

from django.db import models


class DateTimeUUIDModel(models.Model):
    """ A base model with created and edited datetime fields """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    edited = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class FieldWorker(DateTimeUUIDModel):
    CHOICES = [
        (1, 'Harvest'),
        (2, 'Pruning'),
        (3, 'Scouting'),
        (4,'Other')
    ]
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    function = models.CharField(max_length=40, choices=CHOICES)

    def __str__(self):
        return self.first_name
