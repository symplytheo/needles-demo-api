from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "categories", views.CategoryListCreate.as_view(), name="categories-list-create"
    ),
    path("posts", views.PostListCreate.as_view(), name="posts-list-create"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail"),
    path("comments", views.CommentListCreate.as_view(), name="comments-list-create"),
    path("replies", views.ReplyCreate.as_view(), name="replies-create"),
]
