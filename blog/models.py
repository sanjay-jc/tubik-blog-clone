from django.db import models
from .utils import Base_model
from django.utils.text import slugify
from uuid import uuid4
# Create your models here.


class Category(Base_model):
    category_name = models.CharField(max_length=255)
    slug_field = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        print('11',str(uuid4())[:10])
        if not self.slug_field:
            self.slug_field = slugify(self.category_name+str(uuid4())[:10])[:20]

        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.category_name
    

    def clean_category_name(self,*args,**kwargs):
        pass


