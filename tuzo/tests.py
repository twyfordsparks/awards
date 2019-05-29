from django.test import TestCase
from .models import *
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):

        self.image= Image(name = 'black',caption ='image of a black man')
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def tearDown(self):
        Image.objects.all().delete()

class PostTestClass(TestCase):
    def setUp(self):

        self.post= Post(title = 'admin',content ='juju',author = 'me')
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
    def test_save_post(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
    def test_delete_post(self):
        self.post.save_post()
        self.post.delete_post()
        posts=Posts.objects.all()
        self.assertTrue(len(posts)==0)
