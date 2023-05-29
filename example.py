from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Odiljon Toirjonov"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "1",
    "signup_ts": "2005-05-09 14:50",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)
print(user.name)
