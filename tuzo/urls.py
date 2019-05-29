from django.conf.urls import url
from .views import PostListView,PostCreateView,PostUpdateView,PostDeleteView,PostDetailView
from . import views

urlpatterns=[
    url('^$',PostListView.as_view(),name = 'home'),
    url(r'^post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    url(r'^post/new/',PostCreateView.as_view(),name = 'post-create'),
    url(r'^post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    url(r'^post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
]
