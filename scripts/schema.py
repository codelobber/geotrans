import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Point as PointModel

class Point(MongoengineObjectType):

    class Meta:
        model = PointModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    point = graphene.Field(Point)
    all_points = MongoengineConnectionField(Point)

class Add(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        latitude = graphene.String()
        longitud = graphene.String()
        phone = graphene.String()
        due = graphene.DateTime()

    success = graphene.Boolean()
    result = graphene.Field(lambda: Point)

    def mutate(root, info, name, latitude, longitud, phone, due):
        result = PointModel(name = name, latitude = latitude, longitud = longitud, phone = phone, due = due)
        result.save()
        success = True
        return Add(result=result, success=success)

class Mutations(graphene.ObjectType):
    add = Add.Field()


schema = graphene.Schema(query=Query, mutation=Mutations, types=[Point])