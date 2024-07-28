import factory
from django.contrib.auth.models import User
from apps.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test_user'
    password = 'test_password'
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'test_title'
    subtitle = 'test_subtitle'
    slug = 'test_slug'
    author = factory.SubFactory(UserFactory)
    content = 'test_content'
    status = 'test_published'
