from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
