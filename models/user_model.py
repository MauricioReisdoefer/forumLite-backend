from fastjson_db import JsonModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(JsonModel):
    _id: int | None
    name: str = ""
    _password: str = ""

    @property
    def password(self):
        return self._password 

    @password.setter
    def password(self, plain_password: str):
        self._password = generate_password_hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        return check_password_hash(self._password, plain_password)