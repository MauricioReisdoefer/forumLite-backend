from fastjson_db import JsonModel
from fastjson_db.foreignkey import ForeignKey
from .user_model import User
from .topic_model import Topic

class Post(JsonModel):
    _id: int | None
    title: str = ""
    text: str = ""
    user_id: ForeignKey[User] = ForeignKey(User)
    topic_id: ForeignKey[Topic] = ForeignKey(Topic)