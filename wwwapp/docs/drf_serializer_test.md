* ### from wwwapp.models import Person, Stanowisko
  ### from wwwapp.serializers import PersonModelSerializer
  ### from rest_framework.renderers import JSONRenderer
  ### from rest_framework.parsers import JSONParser

stanowisko = Stanowisko(nazwa='plac', opis='opis stanohehe')\
stanowisko.save()

person = Person(imie='Nikita', nazwisko='Oszejko', stanowisko=stanowisko, plec=3)\
person.save()

serializer = PersonModelSerializer(person)\
serializer.data
> {'id': 2, 'imie': 'Nikita', 'nazwisko': 'Oszejko', 'plec': Person.plci.INNE, 'stanowisko': 2}

content = JSONRenderer().render(serializer.data)
content
> {"id":2,"imie":"Nikita","nazwisko":"Oszejko","plec":3,"stanowisko":2}'

### import io

stream = io.BytesIO(content)\
data = JSONParser().parse(stream)\

deserializer = PersonModelSerializer(data=data)\
deserializer.is_valid()
> True

deserializer.errors
> {}

deserializer.fields
> {'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(), 'plec': ChoiceField(choices=<enum 'plci'>, default=Person.plci.INNE), 'stanowisko': PrimaryKeyRelatedField(queryset=<QuerySet [<Stanowisko: Stanowisko object (1)>, <Stanowisko: Stanowisko object (2)>]>)}

deserializer.validated_data
> OrderedDict([('imie', 'Nikita'), ('nazwisko', 'Oszejko'), ('plec', Person.plci.INNE), ('stanowisko', <Stanowisko: Stanowisko object (2)>)])

deserializer.save()
deserializer.data
> {'id': 4, 'imie': 'Nikita', 'nazwisko': 'Oszejko', 'plec': Person.plci.INNE, 'stanowisko': 2}

