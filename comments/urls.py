from django.urls import path

from . import views


urlpatterns = [
    path('', views.CommentViewSet.as_view({'get': 'list'}), name='list_comment'),
    path('', views.CommentViewSet.as_view({'post': 'create'}), name='list_post'),
    path('<int:id>/', views.CommentViewSet.as_view({'get': 'retrieve'}), name='create_post'),
    path('<int:id>/', views.CommentViewSet.as_view({'delete': 'remove'}), name='delete_post'),
]

