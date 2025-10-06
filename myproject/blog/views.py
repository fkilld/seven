from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import  login
from django.db.models import Q 
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView

# Create your views here.


def home(request):
    blogs = Blog.objects.filter(is_published=True)
    categories  = Category.objects.all()
    search_query =request.GET.get('search')
    print(search_query)
    if search_query:
        blogs = blogs.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__username__icontains=search_query) 
        )
    
    
    category_filter =request.GET.get('search')
    print(category_filter)
    if category_filter:
        blogs = blogs.filter(
            category__id=category_filter
        )
        
    paginator =Paginator(blogs,5)
    page_number  = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    

    

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_filter
    }
    return render(request, 'home.html', context)
    

    
    
    
# def blog_detail_view(request, pk):
    

#     # Increment views
#     blog.views += 1
#     blog.save()

#     # Prepare context
#     comment_form = CommentForm()
#     comments = blog.comments.filter(parent=None)

#     user_liked = False
#     if request.user.is_authenticated:
#         user_liked = BlogLike.objects.filter(user=request.user, blog=blog).exists()

#     likes_count = blog.likes.count()

#     context = {
#         'blog': blog,
#         'comment': comments,
#         'comment_form': comment_form,
#         'user_liked': user_liked,
#         'likes_count': likes_count,
#     }

#     return render(request, 'blog/detail.html', context)
    
class BlogDetailView(DetailView):
    
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        blog = self.get_object()
        blog.views +=1
        blog.save()
        
        context['comment'] = blog.comments.filter(parent=None)
        context['comment_form'] = CommentForm()
        if self.request.user.is_authenticated:
            context['user_liked'] =BlogLike.objects.filter(
                user=self.request.user,
                blog=blog
            ).exists()
            
        context['likes_count'] = blog.likes.count()
        return context 
        
        
    
    

# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             return redirect('blog_detail', pk=blog.pk)  # Adjust redirect as needed
#     else:
#         form = BlogForm()
    
#     return render(request, 'blog/create.html', {'form': form})


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/create.html'
    def form_valid(self,form):
        form.instance.author =  self.request.user
        return super().form_valid(form)    
# @login_required
# def update_blog(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)

#     if blog.author != request.user:
#         return HttpResponseForbidden("You are not allowed to edit this blog post.")

#     if request.method == 'POST':
#         form = BlogForm(request.POST, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_detail', pk=blog.pk)  # Update with your detail view
#     else:
#         form = BlogForm(instance=blog)

#     return render(request, 'blog/edit.html', {'form': form})
class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/edit.html'
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author
    
    
    
# @login_required
# def delete_blog(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)

#     if blog.author != request.user:
#         return HttpResponseForbidden("You are not allowed to delete this blog post.")

#     if request.method == 'POST':
#         blog.delete()
#         return redirect('blog_list')  # Replace with your actual blog list view name

#     return render(request, 'blog/delete.html', {'blog': blog})



class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog

    template_name = 'blog/delete.html'
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'categories/list.html', {'categories': categories})
    
class CategoryListView(ListView):
    model = Category

    template_name = 'categories/list.html'
    context_object_name =  'categories'
        
        
        
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # login(request,user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request,'account/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'your profile has been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        