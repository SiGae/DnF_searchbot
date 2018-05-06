from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def keyboard(request):
    return JsonResponse(
        {
            'message' : {
                'text' : '검색하실 아이템의 이름을 말해주세요'
            },
            'type': 'text'
        }
    )