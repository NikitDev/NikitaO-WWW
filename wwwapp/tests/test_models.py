from django.test import TestCase
from django.urls import reverse

from ..models import Person, Stanowisko


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        stanowisko = Stanowisko.objects.create(nazwa='stanowisk', opis='krotki opis')
        Person.objects.create(imie='Nikit', nazwisko='Oszejk', stanowisko=stanowisko)

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('imie').max_length
        self.assertEqual(max_length, 64)

    def create_two_persons_and_check_ids(self):
        stanowisko1 = Stanowisko.objects.create(nazwa='stanowisko1', opis='opis stanowisko1')
        stanowisko2 = Stanowisko.objects.create(nazwa='stanowisko2', opis='opis stanowisko2')
        osoba1 = Person.objects.create(imie='Person1', nazwisko='Naziwsko1', stanowisko=stanowisko1)
        osoba2 = Person.objects.create(imie='Person2', nazwisko='Naziwsko2', stanowisko=stanowisko2)

        self.assertEqual(osoba2.id, 2)

    class ExampleViewTest(TestCase):
        def test_get(self):
            response = self.client.get(reverse('wwwapp:test'))
            self.assertEqual(response.status_code, 200)

        def test_post(self):
            response = self.client.post(reverse('wwwapp:test'))
            self.assertEqual(response.status_code, 201)
