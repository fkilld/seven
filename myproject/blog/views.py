from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import  login
from django.db.models import Q 
from django.core.paginator import Paginator
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

