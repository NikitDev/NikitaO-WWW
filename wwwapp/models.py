from django.db import models


class Stanowisko(models.Model):
    nazwa = models.CharField(blank=False, max_length=64)
    opis = models.CharField(max_length=64)


class Person(models.Model):
    class plci(models.IntegerChoices):
        KOBIETA = 1
        MEZCZYZNA = 2
        INNE = 3

    imie = models.CharField(blank=False, max_length=64, null=True)
    nazwisko = models.CharField(blank=True, max_length=64, null=True)
    plec = models.IntegerField(choices=plci.choices, default=plci.INNE)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
