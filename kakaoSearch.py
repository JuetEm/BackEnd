#LocaleSearcher.py
import urllib.request
import json
from kakaoLocale import KakaoLocale

key ='07476f54b7a2a97622b3dc1caeacf933'
site='https://dapi.kakao.com/v2/local/search/keyword.json'
auth_key="KakaoAK "+ key
auth_header = "Authorization"

def KakaoSearchLocale(query, pSize, pPage):
    global key
    global site
    global auth_key
    global auth_header
    query = urllib.parse.quote(query)
    query_str = site+"?"+"query="+query
    size = "&size="+pSize
    page = "&page="+pPage
    query_str+size+page
    request = urllib.request.Request(query_str)
    request.add_header(auth_header,auth_key)
    response = urllib.request.urlopen(request) #웹 서버에 요청
    rescode = response.getcode()
    print('rescode : {}'.format(rescode))
    if(rescode == 200):
        res = response.read().decode('utf-8')
        jres = json.loads(res)
        # print('jres : {}'.format(jres))
        if jres == None:
            return []
        locales =[]
        for jloc in jres['documents']:
            print("jResult: {}, {}".format(jloc['phone'],jloc.get('phone')))
            """ print("jloc['place_name'] : ".format(jloc['place_name']))
            print("jloc['phone'] : ".format(jloc['phone']))
            print("jloc['place_url'] : ".format(jloc['place_url']))
            print("jloc['address_name'] : ".format(jloc['address_name']))
            print("jloc['road_address_name'] : ".format(jloc['road_address_name']))
            print("jloc['x'] : ".format(jloc['x']))
            print("jloc['y'] : ".format(jloc['y'])) """
            print("jloc : {}".format(jloc))
            locale = KakaoLocale.MakeLocale(jloc)
            if(locale!=None):
                locales.append(locale)
        return locales
    else:
        print("Error Code:" + rescode)
        return []