from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet, MyAdsListAPIView

router = SimpleRouter()
router.register("ads", AdViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("ads/me/", MyAdsListAPIView.as_view()),
] + router.urls
