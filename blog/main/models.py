from django.db import models
from django.utils import timezone

class TimeStampMixin(models.Model):
    '''
    Class for adding timestamps to django fields.
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True