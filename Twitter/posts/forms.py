from django import forms
from posts.models import Post, Comment
from user_auth.models import User



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
    #     widgets = {
    #         'post_id_hidden': forms.HiddenInput()
    #     }
    # # post_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'required': False}))

    post_id_hidden = forms.IntegerField(widget=forms.HiddenInput(),)