from django.shortcuts import render, redirect

# Create your views here.
from Rating.forms import RatingForm
from Rating.models import RatingList, RatingSum


def rating_create(request, post_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            rating_sum = RatingSum.objects.filter(post_id=post_id).first()
            if not rating_sum:
                rating_sum = RatingSum.objects.create(post_id=post_id, amount=0, voted_amount=0)
            rating_sum.amount += int(request.POST['sum'])
            rating_sum.voted_amount += 1
            rating_sum.save()
            return redirect('post_detail', post_id)


