from django.test import TestCase
from django.urls import reverse

from ..models import Person, Stanowisko
import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class PersonModelTest(TestCase):
    def setUp(self):
        self.stanowisko = Stanowisko.objects.create(nazwa='stanowisk', opis='krotki opis')
        self.person = Person.objects.create(imie='Nikit', nazwisko='Oszejk', stanowisko=self.stanowisko)

    def test_first_name_label(self):
        field_label = self.person._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        max_length = self.person._meta.get_field('imie').max_length
        self.assertEqual(max_length, 64)

    def test_create_two_persons_and_check_ids(self):
        stanowisko1 = Stanowisko.objects.create(nazwa='stanowisko1', opis='opis stanowisko1')
        stanowisko2 = Stanowisko.objects.create(nazwa='stanowisko2', opis='opis stanowisko2')
        osoba1 = Person.objects.create(imie='Person1', nazwisko='Naziwsko1', stanowisko=stanowisko1)
        osoba2 = Person.objects.create(imie='Person2', nazwisko='Naziwsko2', stanowisko=stanowisko2)
        self.assertEqual(osoba1.stanowisko, stanowisko1)
        self.assertEqual(osoba2.stanowisko, stanowisko2)


class ExampleViewTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse('wwwapp:test'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post(reverse('wwwapp:test'))
        self.assertEqual(response.status_code, 201)


client = APIClient()


class OsobyTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345')
        Token.objects.create(user=self.user)
        self.stanowisko = Stanowisko.objects.create(nazwa='Testowa')

    def test_create_osoba(self):
        url = reverse('wwwapp:persons_detail')
        data = [{
            'imie': 'Nikit',
            'nazwisko': 'Oszej',
        }]
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().imie, 'Nikit')
        client.force_authenticate(user=None)

    def test_token_auth(self):
        url = reverse('wwwapp:stanowisko', kwargs={'pk': self.stanowisko.id})
        response = client.get(url, headers={'AUTHORIZATION': f'Bearer {self.user.auth_token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)




