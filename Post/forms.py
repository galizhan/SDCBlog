from django.forms import ModelForm
from django import forms
from Post.models import Post
from django.utils.translation import gettext, gettext_lazy as _


class PostForm(ModelForm):
    error_messages = {
        'less_than_five': _("Title less than 5 chars"),
    }

    class Meta:
        model = Post
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError(
                self.error_messages['less_than_five'],
                code='less_than_five',
            )
        return title
