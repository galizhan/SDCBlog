from django import forms

from Post.models import Post
from Rating.models import RatingList


class RatingForm(forms.ModelForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = RatingList
        fields = '__all__'