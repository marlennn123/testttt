from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='signup'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile-detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),

    path('carmake/', CarMakeViewSet.as_view({'get': 'list', 'post': 'create'}), name='carmake-list'),
    path('carmake/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='carmake-detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model-list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='model-detail'),

    path('car/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('car/<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car-detail'),

    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}), name='bet-list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bet-detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
]
