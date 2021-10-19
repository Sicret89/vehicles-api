from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Car(models.Model):
    make = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text="Max 100 characters.",
    )
    model = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text="Max 100 characters.",
    )

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        unique_together = (
            "make",
            "model",
        )


class Rate(models.Model):
    car_id = models.ForeignKey(Car, related_name="rates", on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=False,
    )

    def __str__(self):
            return f"{self.car_id} {self.rating}"
