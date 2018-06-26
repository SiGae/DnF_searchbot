import json
import urllib.request
import urllib.parse
import ssl
import app.bot_private as code

def NumberSlice(number) -> str:
    return format(number, ",")

def SearchAuction(itemName, search_type) -> str:
    item_name = itemName
    if search_type == 'full' and " " in item_name:
        item_name = "\'" + item_name + "\'"
    request_url = 'https://api.neople.co.kr/df/auction?sort=unitPrice:asc&'
    param = urllib.parse.urlencode(
        {
            'itemName': item_name,
            'limit': 50,
            'wordType': search_type,
            'apikey': code.dnfAppKey
        }
    )
    param = param.replace("+", "%20").replace("%27", "\"")
    try:

        ssl._create_default_https_context = ssl._create_unverified_context
        urlOpen = urllib.request.urlopen(request_url + param)
        print(request_url+param)
        infoJSON = json.loads(urlOpen.read().decode('utf-8'))

        k = 0
        i = 10
        a = ''
        check = True
        if len(infoJSON['rows']) < 10:
            i = len(infoJSON['rows'])
            check = False
        elif len(infoJSON['rows']) == 0:
            a = '해당 아이템이 존재하지 않습니다.\n검색 방법 변경을 원할시 채팅창에 \'검색\'을 입력 해주시길 바랍니다.'
            return a
        else:
            i = 10

        if infoJSON['rows'][0]['unitPrice']==0:
            while k < 5:
                if infoJSON['rows'][k]['unitPrice']==0:
                    k +=1
                    if check == True:
                        i += 1
                else:
                    break

        while k < i:
            a += '이름 : {}\n'.format(infoJSON['rows'][k]['itemName'])
            a += '개당 가격 : {}\n'.format(NumberSlice(infoJSON['rows'][k]['unitPrice']))
            a += '총액 : {}\n'.format(NumberSlice(infoJSON['rows'][k]['currentPrice']))
            a += '수량 : {}\n'.format(NumberSlice(infoJSON['rows'][k]['count']))
            a += '\n'
            k += 1
        a += '검색 방법 변경을 원할시 채팅창에 \'검색\'을 입력 해주시길 바랍니다.'

    except Exception as ee:
        print(ee)
        a = '3해당 아이템이 존재하지 않습니다.\n검색 방법 변경을 원할시 채팅창에 \'검색\'을 입력 해주시길 바랍니다.'
    return a

#a = input("입력 : ")
#print(SearchAuction(a, 'full'))