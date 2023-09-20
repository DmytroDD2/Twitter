from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, User
from django.views.generic import ListView, DetailView,CreateView
from posts.forms import PostForm, CommentForm

from django.urls import reverse, reverse_lazy
class TwitterListView(ListView):
    model = Post
    template_name = 'posts/Тwitter_list.html'
    context_object_name = 'posts'# Зміна назви змінної


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "posts/add_post.html"
    success_url = reverse_lazy('Twitter_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post_id_hidden = post
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('post_detail', args=[post_id])







class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(pk=self.object.pk)
        context["comment_text"] = Comment.objects.filter(post_id_hidden=self.object)
        return context


