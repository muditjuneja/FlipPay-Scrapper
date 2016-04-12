from datetime import datetime
# from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer


item1 = Item(name='watch', properties={'qty': 1, 'color': 'black'}, price=500,
            image_url='https://google.com/image?woei.jpg',
            item_url='https://google.com/image?lsfieo.jpg',
            status='under process')
item2 = Item(name='deo', properties={'qty': 1, 'color': 'red'}, price=200,
            image_url='https://google.com/image?werdei.jpg',
            item_url='https://google.com/image?lsfwero.jpg',
            status='under process')
item3 = Item(name='soap', properties={'qty': 2, 'color': 'orange'}, price=100,
            image_url='https://google.com/image?wosfsi.jpg',
            item_url='https://google.com/image?lsfoijhnmeo.jpg',
            status='under process')

order1 = Order(id=1, name='order1', value=800, items=[item1, item2, item3],
               order_date=datetime(2016, 3, 1).date(), seller='flipkart')

serialized_order = OrderSerializer(instance=order1)

print(serialized_order.data)

json = JSONRenderer().render(serialized_order.data)
print(json)
