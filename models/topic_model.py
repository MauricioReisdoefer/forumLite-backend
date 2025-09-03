from fastjson_db import JsonModel
from fastjson_db.foreignkey import ForeignKey
from.user_model import User
from dataclasses import dataclass

@dataclass
class Topic(JsonModel):
    _id: int | None
    title: str = ""
    description: str = ""
    user_id: ForeignKey[User] = ForeignKey(User)