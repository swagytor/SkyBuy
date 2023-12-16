from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from ads.models import Ad, Comment
from ads.permissions import IsOwnerOrAdmin
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'price']
    search_fields = ['title', '$description']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action in ['create', 'retrieve']:
            permissions_classes = [IsAuthenticated]
        else:
            permissions_classes = [AllowAny]

        return [permission() for permission in permissions_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action in ['create', 'retrieve']:
            permissions_classes = [IsAuthenticated]
        else:
            permissions_classes = [AllowAny]

        return [permission() for permission in permissions_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class MyAdsListAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'price']
    search_fields = ['title', '$description']

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)
