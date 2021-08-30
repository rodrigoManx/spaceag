import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from app import models


class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self.length


class FieldWorker(DjangoObjectType):
    class Meta:
        model = models.FieldWorker
        exclude_fields = ('created', 'edited')
        filter_fields = ('name', )
        interfaces = (Node, )
        connection_class = Connection


class Query(graphene.ObjectType):
    all_field_woker = DjangoFilterConnectionField(FieldWorker)
    field_worker = Node.Field(FieldWorker)
    node = Node.Field()


schema = graphene.Schema(
    query=Query,
)
