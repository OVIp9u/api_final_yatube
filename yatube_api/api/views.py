from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User, Follow
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import AuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)

class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет подписок"""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, AuthorOrReadOnly,)

class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        """Метод выбора комментариев по посту"""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод создания комментария"""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)