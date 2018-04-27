import json
import falcon
from models.store import StoreModel
from models.item import ItemModel


class ItemResource:
    def on_post(self, req, resp, name):
        price = req.get_param('price')
        store_id = req.get_param('store_id')
        if not self.session.query(ItemModel).filter(ItemModel.name==name).first():
            item = ItemModel(name=name, price=price, store_id=store_id)
            self.session.add(item)
            self.session.commit()
            resp.body = json.dumps(item.json())
            resp.status = falcon.HTTP_201
        else:
            raise falcon.HTTPBadRequest(description='this item name already exists')

    def on_put(self, req, resp, name):
        price = req.get_param('price')
        store_id = req.get_param('store_id')
        item = self.session.query(ItemModel).filter(ItemModel.name==name).first()
        if not item:
            item = ItemModel(name=name, price=price, store_id=store_id)
            self.session.add(item)
        else:
            item.price = price
            item.store_id = store_id
            self.session.flush()
        self.session.commit()
        resp.body = json.dumps(item.json())
        resp.status = falcon.HTTP_200

    def on_get(self, req, resp, name):
        item = self.session.query(ItemModel).filter(ItemModel.name==name).first()
        if item:
            resp.body = json.dumps(item.json())
        else:
            raise falcon.HTTPNotFound(description='this item name not exist')

    def on_delete(self, req, resp, name):
        item = self.session.query(ItemModel).filter(ItemModel.name==name).first()
        if item:
            self.session.delete(item)
            self.session.commit()
            resp.body = json.dumps({'message':'Item deleted'})
        else:
            raise falcon.HTTPNotFound(description='this item name not exist')


class ItemListResource:
    def on_get(self, req, resp):
        items = []
        for item in self.session.query(ItemModel).all():
            items.append({'name':item.name, 'price':item.price})
        resp.body = json.dumps({'items':items})

