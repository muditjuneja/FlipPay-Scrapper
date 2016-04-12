from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from .tasks import flipkart, jabong, amazon
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class OrderViewSet(ViewSet):
    permission_classes = (permissions.AllowAny, )

    def order_post(self, request, name):
        """
        responsds to POST requests sent at `/scraper/<name>`
        :param request: HTTP request object
        :param name: string, name of the vendor
        :return: Response object with JSON response to the request
        """
        name = name.lower()

        html_string = request.data["html_string"]
        #print html_string;

        # with open('post_data.txt', 'w') as f:
        #     f.write(html_string)

        if html_string:
            flag = False
            if name == 'flipkart':
                orders = flipkart(html_string)
                flag = True
            elif name == 'jabong':
                orders = jabong(html_string)
                flag = True
            elif name == 'amazon':
                orders = amazon(html_string)
                flag = True
            else:
                orders = []
            if flag:
                serialized_orders = OrderSerializer(orders, many=True)
                data = {"status_message": "orders fetched successfully",
                        "data": serialized_orders.data}
            else:
                data = {"status_message": "vendor currently not supported",
                        "data": {}}
            http_status = status.HTTP_200_OK
        else:
            data = {"status_message": "html string not provided",
                    "data": {}}
            http_status = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_status)

    def order_get(self, request, name):
        """
        responsds to get requests sent at `/scraper/<name>`
        :param request: HTTP request object
        :param name: string, name of the vendor
        :return: Response object with JSON response
        """
        if name == 'flipkart':
            orders = flipkart()
            serialized_orders = OrderSerializer(orders, many=True)
            data = {"status_message": "orders fetched successfully",
                    "data": serialized_orders.data}
        elif name == 'jabong':
            orders = jabong()
            serialized_orders = OrderSerializer(orders, many=True)
            data = {"status_message": "orders fetched successfully",
                    "data": serialized_orders.data}
        else:
            data = {"status_message": "vendor currently not supported",
                    "data": {}}
        http_status = status.HTTP_200_OK
        return Response(data, status=http_status)
