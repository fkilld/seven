from django.contrib import admin
from .models import Blog,Category,Profile,Comment,Tag,BlogLike
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
      
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
      
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
      

      
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
      
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
@admin.register(BlogLike)
class BlogLikeAdmin(admin.ModelAdmin):
    pass
      
