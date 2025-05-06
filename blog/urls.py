from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list_view' ),
    path('blogpost/<int:pk>/', BlogDetailView.as_view(), name='blog_detail_view'  ),
]