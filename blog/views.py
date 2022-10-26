from django.shortcuts import render
from blog.models import Post

def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    post_qs = Post.objects.all()
    return render(request, 'blog/index.html', {
        "post_list":post_qs
    })
