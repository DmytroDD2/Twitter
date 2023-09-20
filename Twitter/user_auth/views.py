from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from user_auth.forms import CustomUserCreateForm, LoginForm


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
