from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Blogpost(models.Model):
    STATUS_CHOICES= ( ('0', 'Draft'), ('1', 'Publish'),)


    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField(max_length=5000, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    created_on = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    featured = models.BooleanField()

    def get_absolute_url(self):
        return reverse('blog:blogpost',
        args=[self.slug])

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40, default="")
    phone = models.CharField(max_length=15, default="")
    desc = models.TextField(max_length=1500, default="")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    commentfield = models.TextField()
    post = models.ForeignKey(Blogpost, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username