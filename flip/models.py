from __future__ import unicode_literals


class Order(object):
    """
    Defines an order which has certain items and a total value
    """
    def __init__(self, id, name, value, items, order_date, seller):
        self.id = id
        self.name = name
        self.value = value
        self.items = items
        self.order_date = order_date
        self.seller = seller

    def __unicode__(self):
        return self.name


class Item(object):
    """
    Defines an item object which is part of the order
    """
    def __init__(self, name, properties, price, image_url, item_url,
                 status):

        self.name = name
        self.properties = properties
        self.price = price
        self.image_url = image_url
        self.item_url = item_url
        self.status = status

    def __unicode__(self):
        return self.name
