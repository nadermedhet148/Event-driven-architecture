import json

class UserCreated:

    def __init__(self , name , userId):
        self.name = name
        self.userId = userId
    
    def to_string(self):
        return  json.dumps({
            "name": self.name,
            "userId": self.userId,
        })

