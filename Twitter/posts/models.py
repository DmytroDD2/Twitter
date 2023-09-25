from django.db import models
from user_auth.models import User



class BaseClas(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Post(BaseClas):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)

    likes = models.ManyToManyField(User, related_name='post_detail')

    def number_of_likes(self):
        return self.likes.count()

class Comment(BaseClas):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    post_id_hidden = models.ForeignKey(Post, on_delete=models.CASCADE)


