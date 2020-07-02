from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer



class PostViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    #perimission_classes=(permissions.IsAuthenticated,)
    #permission_classes=(IsAuthorOrReadOnly,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
