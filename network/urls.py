from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PostListCreateView, CommentCreateView, LikeToggleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('comments/', CommentCreateView.as_view(), name='comments'),
    path('posts/<int:post_id>/like/', LikeToggleView.as_view(), name='like_toggle'),
]
