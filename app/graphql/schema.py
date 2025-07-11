import strawberry
from app.resolvers.resolvers import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
