from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from app.db.session import get_db

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Yummi-Go API!"}
