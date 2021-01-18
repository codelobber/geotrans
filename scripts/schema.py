import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Point as PointModel
from models import Config as ConfigModel

class Point(MongoengineObjectType):

    class Meta:
        model = PointModel
        interfaces = (Node,)

class Config(MongoengineObjectType):

    class Meta:
        model = ConfigModel
        interfaces = (Node,)

class Querys(graphene.ObjectType):
    node = Node.Field()
    point = graphene.Field(Point)
    all_points = MongoengineConnectionField(Point)
    config = graphene.List(Config, version = graphene.Int())
    all_configurations = MongoengineConnectionField(Config)

    def resolve_config(self, info, version):
        return ConfigModel.objects.filter(version__exact=version)

class Add(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        latitude = graphene.String()
        longitud = graphene.String()
        phone = graphene.String()
        due = graphene.DateTime()

    success = graphene.Boolean()
    
    def mutate(root, info, name, latitude, longitud, phone, due):
        PointModel.objects(phone=phone).update(set__name = name, set__latitude = latitude, set__longitud = longitud, set__due = due, upsert=True)
        success = True
        return Add(success=success)

class Configurator(graphene.Mutation):
    class Arguments:
        version = graphene.Int()
        isDayPeriodAllowed = graphene.Boolean()
        allowedRadius = graphene.Int()

    success = graphene.Boolean()
    
    def mutate(root, info, name, latitude, longitud, phone, due):
        ConfigModel.objects.objects(version=version).update(set__isDayPeriodAllowed = isDayPeriodAllowed, set__allowedRadius = allowedRadius, upsert=True)
        success = True
        return Add(success=success)

class Mutations(graphene.ObjectType):
    add = Add.Field()
    config = Configurator.Field()


schema = graphene.Schema(query=Querys, mutation=Mutations, types=[Point])