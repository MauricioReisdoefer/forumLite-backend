from fastjson_db import JsonModel

class Topic(JsonModel):
    _id: int | None
    title: str = ""
    description: str = ""