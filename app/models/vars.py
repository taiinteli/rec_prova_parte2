import pydantic

class BlogPostRequest(pydantic.BaseModel):
    id: int
    usuario: str
    review: str
    serie_filme: str
    estrelas: int

