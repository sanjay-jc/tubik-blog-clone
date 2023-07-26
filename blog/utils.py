from django.db import models
from django.db.models.query import QuerySet

class Only_active(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=True)
    


class Base_model(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=((True,"Active"),(False,"Inactive")),default=True)

    is_active = Only_active()
    objects = models.Manager()

    
    class Meta:
        abstract = True


