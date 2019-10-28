import graphene
from graphene_django import DjangoObjectType
import core.schema


class Query(core.schema.Query, graphene.ObjectType):
    pass

class Mutation(core.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)