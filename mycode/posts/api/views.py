from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)

from .serializers import (PostListSerializers, PostDetailSerializers,
                          PostCreateSerializers)

from posts.models import post
from .permissions import IsOwnereOrReadOnly
from .pagination import PostPageNumberPagination  # ,PostLimitOffsetPagination
from django.db.models import Q

from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser,
                                        IsAuthenticatedOrReadOnly)


class PostCreateAPIView(CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostCreateSerializers
    permission_classes = (IsAuthenticated, IsAdminUser)


class PostDetailAPIView(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializers
    # lookup_field = 'slug'


class PostDestroyAPIView(DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializers
    # lookup_field = 'slug'
    permission_classes = (IsAdminUser)


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializers
    pagination_class = PostPageNumberPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
                | Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)).distinct()
        return queryset_list


class PostUpdateAPIView(UpdateAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializers
    # lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnereOrReadOnly)
