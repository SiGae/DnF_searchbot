import json
import urllib.request
import urllib.parse
import ssl
import app.bot_private as code


def SearchAuction(itemName, search_type) -> str:
    if itemName == 'full':
        itemName.replace(" ", "%20")
    item_name = itemName
    request_url = 'https://api.neople.co.kr/df/auction?sort=unitPrice:asc&'
    param = urllib.parse.urlencode(
        {
            'itemName': item_name,
            'wordType': search_type,
            'limit': 10,
            'apikey': code.dnfAppKey
        }
    )
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        urlOpen = urllib.request.urlopen(request_url + param)
        infoJSON = json.loads(urlOpen.read().decode('utf-8'))

        k = 0
        a = ''
        while k < 10:
            a += '이름 : {}\n'.format(infoJSON['rows'][k]['itemName'])
            a += '개당 가격 : {}\n'.format(infoJSON['rows'][k]['unitPrice'])
            a += '총액 : {}\n'.format(infoJSON['rows'][k]['currentPrice'])
            a += '수량 : {}\n'.format(infoJSON['rows'][k]['count'])
            a += '\n'
            k += 1
        a += '검색 방법 변경을 원할시 채팅창에 \'검색\'을 입력 해주시길 바랍니다.'

    except:
        a = '해당 아이템이 존재하지 않습니다.\n검색 방법 변경을 원할시 채팅창에 \'검색\'을 입력 해주시길 바랍니다.'
    return a
