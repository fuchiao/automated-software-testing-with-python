import json
import falcon
from models.user import UserModel
class UserRegister:
    def on_post(self, req, resp):
        name = req.get_param('name')
        password = req.get_param('password')
        if self.session.query(UserModel).filter(UserModel.name==name).all():
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"message": "A user with that username already exists"})
        else:
            user = UserModel(name=name, password=password)
            self.session.add(user)
            self.session.commit()
            resp.status = falcon.HTTP_201
            resp.body = json.dumps({'message': 'User created successfully'})

