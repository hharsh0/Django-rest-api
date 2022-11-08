from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.


# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):
#     data = request.data
#     print(data)
#     return Response(data)


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    # serialization manually
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price

    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'new_price'])
        data = ProductSerializer(instance).data

    return Response(data)

# A simple rest api

# def api_home(request, *args, **kwargs):
#     return JsonResponse({"message":"Hi there this is your django api response!!"})
