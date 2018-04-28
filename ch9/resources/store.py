import json
import falcon
from models.store import StoreModel
from models.item import ItemModel


class StoreResource:
    def on_post(self, req, resp, name):
        if not self.session.query(StoreModel).filter(StoreModel.name==name).first():
            store = StoreModel(name=name)
            self.session.add(store)
            self.session.commit()
            resp.body = json.dumps(store.json())
            resp.status = falcon.HTTP_201
        else:
            raise falcon.HTTPBadRequest(description='this store name already exists')

    def on_get(self, req, resp, name):
        store = self.session.query(StoreModel).filter(StoreModel.name==name).first()
        if store:
            resp.body = json.dumps(store.json())
        else:
            raise falcon.HTTPNotFound(description='this store name not exist')

    def on_delete(self, req, resp, name):
        store = self.session.query(StoreModel).filter(StoreModel.name==name).first()
        if store:
            self.session.delete(store)
            self.session.commit()
            resp.body = json.dumps({'message':'Store deleted'})
        else:
            raise falcon.HTTPNotFound(description='this store name not exist')


class StoreListResource:
    def on_get(self, req, resp):
        stores = []
        for store in self.session.query(StoreModel).all():
            items = self.session.query(ItemModel).filter(ItemModel.store_id==store.id).all()
            items = [{'name':item.name, 'price':item.price} for item in items]
            stores.append({'name':store.name, 'items':items})
        resp.body = json.dumps({'stores':stores})

