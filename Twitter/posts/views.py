from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, User
from django.views.generic import ListView, DetailView,CreateView
from posts.forms import PostForm, CommentForm

from django.urls import reverse, reverse_lazy
class TwitterListView(ListView):
    model = Post
    template_name = 'posts/Тwitter_list.html'
    context_object_name = 'posts'# Зміна назви змінної


# def list_social_network(request):
#     users = User.objects.all()
#     posts = Post.objects.all()
#     comments = Comment.objects.all()
#     context = {
#         'users': users,
#         'posts': posts,
#     }
#     return render(request, 'posts/Тwitter_list.html', context)


# def list_comments(request):

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "posts/add_post.html"
    success_url = reverse_lazy('Twitter_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



# def add_post(request):
#     if request.method == 'POST':
#         print(str(5) * 100)
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('user_detail', user_id=post.user.id)
#     else:
#         form = PostForm()
#     return render(request, 'posts/add_post.html', {'form': form})


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




# def add_comment(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES, initial={'post_id': post_id})
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', post_id=post.id)
#     else:
#         form = CommentForm(initial={'post_id': post_id})
#     return render(request, 'posts/add_comment.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(pk=self.object.pk)
        context["comment_text"] = Comment.objects.filter(post_id_hidden=self.object)
        return context


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     users = User.objects.filter(pk=post_id)
#     comments = Comment.objects.filter(post=post_id)
#     context = {
#                'users': users,
#                'comments': comments,
#                'post': post
#     }
#     return render(request, 'posts/post_detail.html', context)