import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

from products.serializers import ProductSerializer

from products.models import Product
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)