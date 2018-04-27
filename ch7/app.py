import falcon
import json
from db import Session
from resources.user import UserRegister, UserAuth

class SQLAlchemySessionManager:
    def process_resource(self, req, resp, resource, params):
        resource.session = Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            if not req_succeeded:
                resource.session.rollback()
            Session.remove()

class Resource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'message':'hello'})

app = falcon.API(middleware=[
    SQLAlchemySessionManager(),
])

r = Resource()
app.add_route('/', r)
app.add_route('/register', UserRegister())
app.add_route('/auth', UserAuth())
