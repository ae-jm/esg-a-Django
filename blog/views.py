from django.shortcuts import render
from blog.models import Post

def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    post_qs = Post.objects.all().order_by("-id")
    return render(request, 'blog/index.html', {
        "post_list":post_qs,
    })

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog\single_post_page.html", {
        "post":post,
    })


