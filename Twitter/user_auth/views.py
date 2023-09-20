from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from user_auth.forms import CustomUserCreateForm, LoginForm
from user_auth.models import User
from posts.models import Post, Comment

class UserDetailView(DeleteView):
    model = User
    template_name = 'posts/user_detail.html'
    context_object_name = 'userr'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        context["comments"] = Comment.objects.filter(user=self.object)
        context['posts'] = Post.objects.filter(user=user_id)
        return context
# def user_detail(request, user_id):
#     userr = get_object_or_404(User, pk=user_id)
#     posts = Post.objects.filter(user=user_id)
#     comments = Comment.objects.filter(user=user_id)
#     context = {
#                'userr': userr,
#                'comments': comments,
#                'posts': posts
#     }
#     return render(request, 'posts/user_detail.html', context)






class RegisterView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('Twitter_list')
    template_name = 'user_auth/registration.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Twitter_list')

    else:
        form = LoginForm()
    return render(request, 'user_auth/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('Twitter_list')
