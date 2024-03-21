from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog/post/list.html"
    
    def post_detail(request, year, month, day, slug):
        post = get_object_or_405(Post, slug = slug, status="published", publish__year = year, publish__month = month,  publish__day = day)
