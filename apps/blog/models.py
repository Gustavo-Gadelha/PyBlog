from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    STATUS_OPTIONS = (
        ('draft', 'Draft'),
        ('published ', 'Published'),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default='draft')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
