from django.shortcuts import render

from api.serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from api import models

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, ) # change to isauth
    http_method_names = ['get']


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)


class Posts(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

    #permission_classes = (AllowAny, ) # change to isauth

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
def post_by_id(request, pk):
    try:
        post = models.Post.objects.filter(created_by=request.user).get(pk=pk)
    except models.Post.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.method == 'DELETE':
        post.delete()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['POST'])
def put_a_like(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
    except models.Post.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    post.like_count += 1

    post.save()

    return Response(status=status.HTTP_200_OK)










