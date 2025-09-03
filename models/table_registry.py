from .user_model import User
from .topic_model import Topic
from .post_model import Post
from fastjson_db import TABLE_REGISTRY, JsonTable

user_table = JsonTable("users.json", User)
topic_table = JsonTable("topic.json", Topic)
post_table = JsonTable("post.json", Post)

TABLE_REGISTRY[User] = user_table
TABLE_REGISTRY[Topic] = topic_table
TABLE_REGISTRY[Post] = post_table