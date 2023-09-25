from django.urls import path

from users.views import UserDetailView, user_followers, UpdateUserView, UseAuthDetailView


urlpatterns = [
    path('user_auth_detail/', UseAuthDetailView.as_view(), name='user_auth_detail'),
    path('update_user/', UpdateUserView.as_view(), name='update_user'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/follow', user_followers, name='user_followers'),
]
