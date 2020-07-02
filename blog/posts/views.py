from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer




class PostList(generics.ListCreateAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #perimission_classes=(permissions.IsAuthenticated,)
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

"""
If you notice, there is quite a bit of repetition here.
 Both Post views and User views
have the exact same queryset and serializer_class .
 Maybe those could be combined
in some way to save code?
Finally we have our URL routes. Make sure to import our
 new UserList , and UserDetail
views. Then we can use the prefix users/ for each.
"""