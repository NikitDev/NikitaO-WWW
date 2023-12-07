import graphene
from graphene_django import DjangoObjectType

from wwwapp.models import Person, Stanowisko


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ('id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'wlasciciel')


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ('id', 'nazwa', 'opis')


class Query(graphene.ObjectType):
    all_teams = graphene.List(StanowiskoType)
    person_by_id = graphene.Field(PersonType, id=graphene.Int(required=True))
    all_persons = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    find_persons_name_by_phrase = graphene.List(PersonType, substr=graphene.String(required=True))
    find_stanowisko_contains = graphene.List(StanowiskoType, text=graphene.String(required=True))

    def resolve_all_teams(root, info):
        return Stanowisko.objects.all()

    def resolve_person_by_id(root, info, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Exception('Invalid person Id')

    def resolve_person_by_name(root, info, name):
        try:
            return Person.objects.get(imie=name)
        except Person.DoesNotExist:
            raise Exception(f'No Person with name \'{name}\' found.')

    def resolve_all_persons(root, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Person"""
        return Person.objects.select_related("team").all()

    def resolve_find_persons_name_by_phrase(self, info, substr):
        return Person.objects.filter(imie__icontains=substr)

    def resolve_find_stanowisko_contains(root, info, text):
        return Stanowisko.objects.filter(nazwa__icontains=text)


schema = graphene.Schema(query=Query)

