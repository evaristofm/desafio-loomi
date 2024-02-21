# from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
#
# from .models import Post, Like
# from .serializers import PostSerializer, LikeSerializer
#
#
# class PostViewSet(ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#
# @api_view(['POST'])
# def post_like(request, pk):
#     #like = Like.objects.create(created_by=request.user)
#
#     post = Post.objects.get(pk=pk)
#     post.likes_count += 1
#     #post.likes.add(like)
#     post.save()
#
#     return JsonResponse({'status': 200})
#
#
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
#
