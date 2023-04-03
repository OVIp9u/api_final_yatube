from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Пермишшн безопасный метод или автор записи"""
    message = 'Нет доступа к записи'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )
