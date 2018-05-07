from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import app.AuctionSearch
# Create your views here.


def keyboard(request):
    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['단어 검색', '첫부분 일치', '전체 일치']
        }
    )


@csrf_exempt
def message(request):
    global search_type

    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name0 = received_json['content']
    type_name = received_json['type']

    if content_name0 == '검색':
        return JsonResponse(
            {
                'message': {
                    'text': '검색 방법을 선택해주세요'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['단어 검색', '첫부분 일치', '전체 일치']
                }
            }
        )
    elif content_name0 == '단어 검색':
        search_type = 'full'
        return JsonResponse(
            {
                'message': {
                    'text': '단어 검색이 선택 되었습니다. 아이템 이름을 입력해주세요.\n(복수 단어 입력시 마지막 단어로 검색이 됩니다.)'
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )
    elif content_name0 == '첫부분 일치':
        search_type = 'front'
        return JsonResponse(
            {
                'message': {
                    'text': '첫부분 일치가 선택 되었습니다. 아이템 이름을 처음부터 정확히 입력해주세요'
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )
    elif content_name0 == '전체 일치':
        search_type = 'match'
        return JsonResponse(
            {
                'message': {
                    'text': '전체 일치를 선택 하셨습니다 아이템 이름을 정확하게 입력해주세요'
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )

    if type_name == 'text' and search_type != "":
        return JsonResponse(
            {
                'message': {
                    'text': app.AuctionSearch.SearchAuction(content_name0, search_type)
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )

    else:
        return JsonResponse(
            {
                'message': {
                    'text': '텍스트만 입력하주시길 바랍니다'
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )