from django.urls import path 

from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('blog/<int:pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('blog/new/',views.BlogCreateView.as_view(),name='blog_create'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:blog_id>/comment/', views.add_comment, name='add_comment'),
    path('blog/<int:blog_id>/like/', views.toggle_like, name='toggle_like'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    
]
