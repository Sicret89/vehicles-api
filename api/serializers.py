from rest_framework import serializers

from api.models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    make = serializers.CharField(
        max_length=100,
        help_text="Max 100 characters."
    )
    model = serializers.CharField(
        max_length=100,
        help_text="Max 100 characters."
    )
    avg_rating = serializers.SerializerMethodField()
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            "id",
            "make",
            "model",
            "avg_rating",
            "rates_number"
        )

    def get_avg_rating(self, obj):
        try:
            return obj.avg_rating
        except AttributeError:
            return None

    def get_rates_number(self, obj):
        try:
            return obj.rates_number
        except AttributeError:
            return None


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(),
        help_text="ID of car to rate."
    )
    rating = serializers.IntegerField(
        min_value=1,
        max_value=5,
        help_text="Rating range from 1 to 5.",
    )

    class Meta:
        model = Rate
        fields = (
            "id",
            "car_id",
            "rating"
        )
