from wwwapp.models import Person, Stanowisko
from wwwapp.serializers import PersonModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

stanowisko = Stanowisko(nazwa='plac', opis='opis stanohehe')
person = Person(imie='Nikita', stanowisko=stanowisko, plec=3)
person.save()
serializer = PersonModelSerializer(person)
serializer.data
{'id': 1, 'imie': 'Nikita', 'nazwisko': None, 'plec': Person.plci.INNE, 'stanowisko': 1}
content = JSONRenderer().render(serializer.data)
content
b'{"id":1,"imie":"Nikita","nazwisko":null,"plec":3,"stanowisko":1}'

import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonModelSerializer(data=data)
deserializer.is_valid()
False
