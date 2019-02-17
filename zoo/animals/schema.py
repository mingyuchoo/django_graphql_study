from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Animal


class AnimalNode(DjangoObjectType):
    class Meta:
        model = Animal
        filter_fields = ['name', 'genus', 'is_domesticated']
        interfaces = (relay.Node, )


class Query(ObjectType):
    animal = relay.Node.Field(AnimalNode)
    all_animals = DjangoFilterConnectionField(AnimalNode)

