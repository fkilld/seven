from django.urls import path 

from .import views
#     path('',include('blog.urls')), path =/blog/new/
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/<int:pk>/',views.profile_detail,name='profile_detail'),
    path('blog/<slug:slug>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('blog/azadd/',views.BlogCreateView.as_view(),name='blog_create'),
    path('blog/<slug:slug>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('blog/<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    
]
