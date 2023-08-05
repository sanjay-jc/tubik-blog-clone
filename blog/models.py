from django.db import models
from .utils import Base_model
from django.utils.text import slugify
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Create your models here.

#local imports 

#3rd party imports

from ckeditor.fields import RichTextField

user = get_user_model()


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
    

    def clean(self):
        print('jelds')
        if len(self.category_name) > 255:
            raise ValidationError('Max length of the category name is 255 chars')
        

class Blog(Base_model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="blog_category")
    created_by = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    slug_field = models.SlugField(null=True,blank=True,max_length=50)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug_field:
            self.slug_field = slugify(uuid4())[:20]
        return super().save(*args,**kwargs)
    

    def clean(self):
        if len(self.title) > 255:
            return ValidationError('Title must be less than 255 characters')
        

    
class Blog_media(Base_model):
    blog = models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
    media = models.FileField(upload_to="blog_media")


    def __str__(self):
        return str(self.blog)
        
    

    

