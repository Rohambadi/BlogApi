from .models import post
from .serializers import PostSerializer
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly, IsAdmin



class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAdmin,)
    queryset = post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = post.objects.all()
    serializer_class = PostSerializer

