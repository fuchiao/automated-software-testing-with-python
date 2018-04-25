import falcon
import json

class Resource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'message':'hello'})

app = falcon.API()

r = Resource()
app.add_route('/', r)
