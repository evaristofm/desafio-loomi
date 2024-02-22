from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from post.models import Post
from comments.models import Like
from post.serializers import PostSerializer


class PostViewSet(ViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        query_set = Post.objects.all()
        return Response(self.serializer_class(query_set, many=True).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None, *args, **kwargs):
        post = get_object_or_404(self.queryset, pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def remove(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs.get('id'))
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    like = Like.objects.create(user=request.user, post=post)

    post.likes_count += 1
    post.likes.add(like)
    post.save()

    return JsonResponse({'status': 200})


# class LikeViewSet(ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#
#     def create(self, request, pk=None, *args, **kwargs):
#         post = Post.objects.get(pk=pk)
#         post.likes_count += 1
#         post.save()
#         return Response({'status': 200})
#
#     def destroy(self, request, pk=None, *args, **kwargs):
#         post = Post.objects.get(pk=pk)
#         post.likes_count -= 1
#         post.save()
#         return Response({'status': 204})
