from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment, Like
from post.models import Post
from comments.serializers import CommentSerializer


class CommentViewSet(ViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.filter(user=self.kwargs.get('pk'))

    def get_object(self):
        queryset = get_object_or_404(self.queryset, pk=self.kwargs.get('pk'))
        return queryset

    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True).data,
                        status=status.HTTP_200_OK)

    def create(self, request):
        request.data['user'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk=None):
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeViewSet(APIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = get_object_or_404(self.queryset, pk=self.kwargs.get('pk'))
        return queryset

    def post(self, request, pk=None, *args, **kwargs):
        post = self.get_queryset()

        if not post.likes.filter(user=request.user):
            like = Like.objects.create(user=request.user)

        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None, *args, **kwargs):
        post = self.get_queryset()
        post.likes_count = post.likes_count - 1
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
