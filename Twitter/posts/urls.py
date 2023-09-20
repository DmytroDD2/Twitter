from django.urls import path

from .views import TwitterListView, CommentCreateView, PostDetailView, PostCreateView
# from users.views import add_user, user_list, user_detail

urlpatterns = [
    path('', TwitterListView.as_view(), name='Twitter_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('posts/<int:post_id>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
]

