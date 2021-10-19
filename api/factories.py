from random import randint

import factory
from faker import Factory

from api.models import Car, Rate

faker = Factory.create()


class CarFactory(factory.Factory):
    class Meta:
        model = Car

    make = factory.Sequence(lambda n: "make_%d" % n)
    model = factory.Sequence(lambda n: "model_%d" % n)


class RateFactory(factory.Factory):
    class Meta:
        model = Rate

    car_id = factory.SubFactory(CarFactory)
    rating = randint(1, 5)
