from multiprocessing import context
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import *
from rest_framework.filters import SearchFilter
import requests
from .serializers import *
import json
from .utils import MultipartJsonParser
# Create your views here.
# class AddShop(viewsets.ViewSet):
class AddShop(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, format=None):
        shopImages = []
        x = json.loads(request.data['shop'])
        # converts querydict to original dict
        # s = dict(request.data)['owner']
        images = dict((request.data).lists())['images']
        # print(images)
        for i in images:
            img = ShopImage(image=i)
            img.save()
            shopImages.append(img.id)
        # print(shopImages)
        ns = Shop.objects.create(**x)
        ns.images.set(shopImages)
        if ns.id:
            shop = ShopSerializer(ns, context={"request":request})
            return Response(shop.data)
        else:
            print("err")
        # z = requests.patch(
        #     'http://localhost:8000/shops/'+str(newShop.json()["id"])+'/',
        #             data={"images":[1,2,3]})
        # print(z.json())

class ShopVS(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

class Search(viewsets.ReadOnlyModelViewSet):
    filter_backends = (SearchFilter,)
    search_fields = ['address']
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer