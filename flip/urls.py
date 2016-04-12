from django.conf.urls import url
from .views import OrderViewSet


urlpatterns = [
    url(r'^(?P<name>[a-zA-Z]+)/?$', OrderViewSet.as_view({"post": "order_post",
                                                    "get": "order_get"}),
        name="order"),
]
