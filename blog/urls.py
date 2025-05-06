from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list_view' ),
    path('blogpost/<int:pk>/', BlogDetailView.as_view(), name='blog_detail_view'  ),
    path('blogpost/new/', BlogCreateView.as_view(), name='blog_create_view' ),
    path('blogpost/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_update_view' ),
    path('blogpost/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete_view' ),
]