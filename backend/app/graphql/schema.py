import strawberry

@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        # Replace this with actual database fetching logic
        return [
            User(id=1, name="John Doe", email="john@example.com"),
            User(id=2, name="Jane Doe", email="jane@example.com"),
        ]

schema = strawberry.Schema(query=Query)