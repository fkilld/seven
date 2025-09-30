from django.db import models  # import Django's model base classes and field types
from django.contrib.auth.models import User  # import the built-in User model provided by Django
from django.urls import reverse  # import reverse to build URLs from named routes
from django.db.models.signals import post_save  # import the post_save signal to run code after saving a model


class Category(models.Model):  # define a Category model to group blog posts
    name = models.CharField(max_length=100, unique=True)  # the category name, must be unique and limited to 100 chars
    description = models.TextField(blank=True)  # optional longer description of the category
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp set once when the category is created

    class Meta:  # metadata for the model
        verbose_name_plural = "Categories"  # use "Categories" as the plural display name in admin and elsewhere

    def __str__(self):  # string representation of the category
        return self.name  # show the category name when converted to a string

    def get_absolute_url(self):  # helper to get the URL for a category detail page
        return reverse('category_detail', kwargs={'pk': self.pk})  # build URL using the category's primary key
        
        
class Profile(models.model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=500,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    avatar = models.ImageField(upload_to='profile_images/',null=True,blank=True,help_text='upload profile picture')
    website = models.URLField(blank=True)
    def __str__(self):  
        return self.user.username  

    def get_absolute_url(self):  
        return reverse('profile_detail', kwargs={'pk': self.pk})  
    