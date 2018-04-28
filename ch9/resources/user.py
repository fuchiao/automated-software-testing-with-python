from datetime import datetime, timedelta
import json
import falcon
import jwt
from models.user import UserModel

TOKEN_EXPIRED_SECONDS=3600
JWT_ENCODE_SECRET='THIS_IS_SECRET'

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

class UserAuth:
    def on_post(self, req, resp):
        name = req.get_param('name')
        password = req.get_param('password')
        user = self.session.query(UserModel).filter(UserModel.name==name).first()
        if user and user.password == password:
            token = jwt.encode({
                    'user_identifier': user.name,
                    'exp': datetime.utcnow()+timedelta(seconds=TOKEN_EXPIRED_SECONDS),
                }, JWT_ENCODE_SECRET, algorithm='HS256').decode("utf-8")
            resp.body = json.dumps({'access_token':token})
        else:
            raise falcon.HTTPUnauthorized('Bad username/password combination', '', None)


class AuthMiddleware:
    def process_resource(self, req, resp, resource, params):
        if isinstance(resource, (UserAuth, UserRegister)):
            return
        try:
            scheme,token=req.get_header('Authorization',default='Bearer ').split(' ')
            jwt.decode(token, JWT_ENCODE_SECRET,
                       verify='True', algorithms=['HS256'],
                       options={'verify_exp': True})
            if scheme != 'Bearer':
                raise falcon.HTTPUnauthorized(description=scheme+' not supported')
        except jwt.DecodeError as err:
            raise falcon.HTTPUnauthorized(description='Bad JWToken')
        except ValueError as err:
            raise falcon.HTTPUnauthorized(description='Bad Authorization Header')

