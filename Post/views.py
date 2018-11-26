from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from Comment.models import Comment
from Post.forms import PostForm
from Post.models import Post
from Rating.models import RatingSum
from Rating.forms import RatingForm

def index(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request, 'post_index.html', {'posts': all_posts})


def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/post/')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def search(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        if not search_text:
            return redirect('post_index')
        filtered_posts = Post.objects.filter(title__contains=search_text)
        return render(request, 'post_index.html', {'filtered_posts': filtered_posts,'found_number': len(filtered_posts)})
    return redirect('post_index')


def detail(request, request_post_id):
    try:
        post = Post.objects.get(pk=request_post_id)
        comments = Comment.objects.filter(post_id=request_post_id)
        rating_sum = RatingSum.objects.filter(post_id=request_post_id).first()
        if not rating_sum:
            rating = 0
        else:
            rating = rating_sum.amount/rating_sum.voted_amount
        rating_form = RatingForm(initial={'post': post})
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'rating': rating, 'rating_form': rating_form})
