# main.py
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from app.auth.dependencies import get_current_user
from app.config.settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_context(request: Request) -> dict:
    user = await get_current_user(request)
    return {"request": request, "user": user}

graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/api/airport")
