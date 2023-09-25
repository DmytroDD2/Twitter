from django.shortcuts import get_object_or_404, HttpResponseRedirect, reverse
from posts.models import Post, Comment, User
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from posts.forms import PostForm, CommentForm
from django.db.models import Count
from django.urls import reverse, reverse_lazy
class TwitterListView(ListView):
    model = Post
    template_name = 'posts/Тwitter_list.html'
    context_object_name = 'postss'
    paginate_by = 6
    def get_queryset(self):
        queryset = super().get_queryset().select_related("user",).annotate(comment_count=Count('comment'))
        return queryset



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context[self.context_object_name]

        context["users"] = User.objects.all()
        return context




class UserFollowingListView(TwitterListView):
    template_name = 'posts/Тwitter_list_following.html'
    def get_queryset(self):
        user = self.request.user
        following_user = user.following.all()
        query = Post.objects.filter(user__in=following_user).prefetch_related("user")
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["following"] = user.following.all().only('username', 'cover_image')
        context["followers"] = user.followers.all().only('username', 'cover_image')
        return context


class UserFollowerListView(UserFollowingListView):
    template_name = 'posts/Тwitter_list_followers.html'





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
        form.instance.post_id_hidden_id = post_id
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('post_detail', args=[post_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        context['post_id'] = post.id
        return context





class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked

        context["users"] = User.objects.filter(pk=self.object.pk)
        context["comment_text"] = Comment.objects.filter(post_id_hidden=self.object)
        context['number_of_comments'] = self.object.comment_set.count()
        return context


def blogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('user_auth_detail')
    template_name = "posts/delete_post.html"



