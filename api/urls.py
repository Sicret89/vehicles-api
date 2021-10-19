from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"popular", views.PopularViewSet, basename="popular")
router.register(r"rate", views.RateViewSet, basename="rate")
router.register(r"cars", views.CarViewSet, basename="cars")


urlpatterns = [url(r"^", include(router.urls))]
