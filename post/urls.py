from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostViewSet.as_view({'get': 'list'}), name='list_post'),
    path('', views.PostViewSet.as_view({'post': 'create'}), name='create_post'),
    path('<int:id>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='retrieve_post'),
    path('<int:id>/', views.PostViewSet.as_view({'delete': 'remove'}), name='delete_post'),
]

