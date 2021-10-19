import json

import requests
from django.test import Client, TestCase
from django.urls import reverse

from .models import Car


class CarsApiTest(TestCase):

    client = Client()

    def setUp(self):
        Car.objects.create(make='Ford', model='Fokus')
        Car.objects.create(make='Audi', model='A3')
        pass

    def test_cars(self):
        cars_response = self.client.get('/cars/')
        self.assertEqual(cars_response.status_code, 200)

    def test_post_rate(self):
        car = Car(id=1, make="BMW", model="Z3")
        car.save()
        rate_post_response = self.client.post('/rate/',
        content_type='application/json', data={"car_id": "1", "rating": "5"})
        self.assertEqual(rate_post_response.status_code, 201)

    def test_popular(self):
        popular_response = self.client.get('/popular/')
        self.assertEqual(popular_response.status_code, 200)

    def test_status_code_from_third_party_api(self):
        make = 'Audi'
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
        response = requests.get(url)
        self.assertEqual(200, response.status_code)

    def test_delete_car_object(self):
        c = Client()
        car = Car.objects.get(model='A3')
        url = f'/cars/{car.id}/'
        response_delete = c.delete(url)
        self.assertEqual(204, response_delete.status_code)

    def test_delete_car_that_does_not_exist_return_error(self):
        c = Client()
        url = f'/cars/99/'
        response_delete = c.delete(url)
        self.assertEqual(404, response_delete.status_code)
