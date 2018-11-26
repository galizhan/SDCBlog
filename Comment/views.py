from django.shortcuts import render, redirect
from Comment.models import Comment


def create(request, post_id):
    print('from ' + str(post_id))
    my_username = request.POST['username']
    my_text = request.POST['text']
    if not my_username or not my_text:
        return redirect('post_detail', post_id)
    print('username is ' + my_username)
    comment = Comment.objects.create(post_id=post_id, username=my_username, text=my_text)
    comment.save()
    return redirect('post_detail', post_id)
