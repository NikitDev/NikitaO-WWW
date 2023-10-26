from rest_framework import serializers

from wwwapp.models import Person, Stanowisko


class PersonModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField()
    plec = serializers.ChoiceField(choices=Person.plci, default=Person.plci.INNE)
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('name', instance.name)
        instance.nazwisko = validated_data.get('shirt_size', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance


class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']
        read_only_fields = ['id']
