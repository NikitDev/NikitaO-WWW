from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Person, Stanowisko
from .serializers import PersonModelSerializer


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonModelSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if person.wlasciciel != request.user:
        print("XDDDDDDDDDDDDDDDD")
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonModelSerializer(person)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if person.wlasciciel != request.user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = PersonModelSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([BearerTokenAuthentication])
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def persons_stanowisko(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        persons = Person.objects.filter(stanowisko=stanowisko)
        serializer = PersonModelSerializer(persons, many=True)
        return Response(serializer.data)
