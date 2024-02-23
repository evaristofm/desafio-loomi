from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(ViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

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

    def retrieve(self, request, id=None):
        post = get_object_or_404(self.queryset, pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def remove(self, request, id=None):
        post = self.queryset.get(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
