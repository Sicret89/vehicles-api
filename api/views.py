import logging

from django.db.models import Avg, Count
from rest_framework import mixins, viewsets

from api.models import Car, Rate
from api.serializers import CarSerializer, RateSerializer

logger = logging.getLogger(__name__)

class CarViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        self.queryset = self.queryset.annotate(avg_rating=Avg("rates__rating"))
        self.queryset = self.queryset.annotate(rates_number=Count("rates__rating"))
        return self.queryset

class RateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ["post"]


class PopularViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
    http_method_names = ["get"]

    def get_queryset(self):
        self.queryset = self.queryset.annotate(avg_rating=Avg("rates__rating"))
        self.queryset = self.queryset.annotate(
            rates_number=Count("rates__rating")
        ).order_by("-rates_number")
        return self.queryset[:10]
