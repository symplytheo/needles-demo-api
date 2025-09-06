from django.http import HttpResponse
from rest_framework import generics
from .serializers import (
    CategorySerializer,
    PostSerializer,
    ReplySerializer,
    CommentSerializer,
    PostDetailSerializer,
)
from .models import Category, Post, Comment, Reply

# Create your views here.


def index(request):
    return HttpResponse("==Blog Index==")


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # disables pagination here


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()  # .order_by('-created_at')
    serializer_class = CommentSerializer


class ReplyCreate(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
