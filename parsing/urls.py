from django.urls import include, path
from rest_framework.routers import DefaultRouter

from parsing.views import NewsViewSet

router = DefaultRouter()
router.register("news", NewsViewSet, basename="news")


urlpatterns = [
    path("", include(router.urls)),
]
