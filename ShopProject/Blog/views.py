from django.shortcuts import render
from .models import Post
from Eshopper.models import Category, Brand
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.filter(parent=None)
    brands = Brand.objects.all()
    paginator = Paginator(posts, 2)
    page_num = request.GET.get('page',1)
    page_objects = paginator.get_page(page_num)
    context = {
        'posts': posts,
        'categories': categories,
        'brands': brands,
        'page_obj': page_objects,
    }
    return render(request, 'Blog/blog.html', context=context)

