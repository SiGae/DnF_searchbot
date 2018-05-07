from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import app.AuctionSearch
# Create your views here.


def keyboard(request):
    return JsonResponse(
        {
            'type': 'text'
        }
    )


@csrf_exempt
def message(request):

    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']

    return JsonResponse(
        {
            'message': {
                'text': app.AuctionSearch.SearchAuction(content_name)
            },
            'keyboard': {
                'type': 'text'
            }
        }
    )