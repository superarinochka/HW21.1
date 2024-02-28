from django.urls import path
from .views import BlogPostListView, BlogPostDeleteView, BlogPostDetailView, BlogPostUpdateView, BlogPostCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('detail/<slug>/', BlogPostDetailView.as_view(), name='detail'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('update/<slug>/', BlogPostUpdateView.as_view(), name='update'),
    path('delete/<slug>/', BlogPostDeleteView.as_view(), name='delete'),
]