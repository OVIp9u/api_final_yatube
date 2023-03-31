from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import GroupViewSet, CommentViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='groups')
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
