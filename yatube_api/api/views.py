from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)

from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer,
    GroupSerializer, PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет подписок"""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrReadOnly,)

    def get_queryset(self):
        """Метод выбора комментариев по посту"""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод создания комментария"""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
