from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *

 


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    print (session_key)

    return_dict.update({1:'hallo'})
    # data = request.POST
    # product_id = data.get("product_id")
    # quantity = data.get("quantity")

    return JsonResponse(return_dict)

