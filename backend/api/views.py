import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

from products.models import Product
# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    # request.body --> HTTP Request => Django
    instance = Product.objects.all().order_by("?").first()
    data = {} 
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])

        # serialization
        data = ProductSerializer(instance).data
    return Response(data)