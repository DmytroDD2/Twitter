from django.urls import path

from .views import TwitterListView, CommentCreateView, PostDetailView, PostCreateView, blogPostLike, UserFollowingListView, UserFollowerListView, DeletePostView
# from users.views import add_user, user_list, user_detail,

urlpatterns = [
    path('', TwitterListView.as_view(), name='Twitter_list'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('following/', UserFollowingListView.as_view(), name='twitter_list_following'),
    path('followers/', UserFollowerListView.as_view(), name='twitter_list_followers'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/like', blogPostLike, name='blogpost_like'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('posts/<int:post_id>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
]

