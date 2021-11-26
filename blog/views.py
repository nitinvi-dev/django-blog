from .models import Post
from django.shortcuts import render


# To retrieve all post(S) data from database.
def get_posts():
    return Post.objects.all()

# Asynchronous function to get data of blogs.
async def post_list(request):
    data = [post for post in get_posts()]
    return render(request, "index.html", {'post_list': data})

# detail function to retrieve specific blog data.
async def post_details(request, slug):
    obj = Post.objects.get(slug=slug)
    return render(request, "post_detail.html", {"post": obj})
