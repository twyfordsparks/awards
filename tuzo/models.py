from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =120)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    # def save_profile(self):
    #     self.save()
    # def delete_profile(self):
    #     self.delete()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})

    def save_post(self):
        self.save()

    def delete_profile(self):
        self.post()

    @classmethod
    def search_project(cls, name):
        pro = Post.objects.filter(title__icontains = name)
        return pro
