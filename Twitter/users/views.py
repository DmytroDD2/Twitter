from django.shortcuts import  get_object_or_404, reverse, HttpResponseRedirect
from django.views.generic import DetailView

from user_auth.models import User
from posts.models import Post, Comment
from django.views.generic.edit import UpdateView



class UpdateUserView(UpdateView):
    model = User
    fields = ['cover_image', 'username', 'email']
    template_name = 'users/update_user.html'
    context_object_name = 'user'


    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context["comments"] = Comment.objects.filter(user=user_id)
        context['posts'] = Post.objects.filter(user=user_id)

        followers = False

        current_user = get_object_or_404(User, id=user_id)
        if current_user.followers.filter(id=user_id).exists():
            followers = True
        context['following'] = User.objects.filter(followers__id=user_id)
        context['users_is_followers'] = followers
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'posts/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        context["comments"] = Comment.objects.filter(user=self.object)
        context['posts'] = Post.objects.filter(user=user_id)

        followers = False

        current_user = get_object_or_404(User, id=self.kwargs["pk"])
        if current_user.followers.filter(id=self.request.user.id).exists():
            followers = True
        context['following'] = User.objects.filter(followers__id=self.request.user.id)
        context['users_is_followers'] = followers
        return context

class UseAuthDetailView(DetailView):
    template_name = 'posts/user_auth_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user
        context["comments"] = Comment.objects.filter(user=user_id)
        context['posts'] = Post.objects.filter(user=user_id)
        return context


def user_followers(request, pk):
    user = get_object_or_404(User, id=request.POST.get("pk"))

    if user.followers.filter(id=request.user.id).exists():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return HttpResponseRedirect(reverse('user_detail', args=[str(pk)]))
