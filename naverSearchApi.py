# 네이버 검색 API 예제 - 블로그 검색
from flask import make_response
import os
import sys
import urllib.request
import json


def NaverSearch(searchType, queyrString):
    client_id = "1vV153w6pttARbNeXGLf"
    client_secret = "VRSERFPRds"
    encText = urllib.parse.quote(queyrString)
    url = "https://openapi.naver.com/v1/search/"+searchType+"?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    # display / Integer / N / 한 번에 표시할 결과 개수(기본값: 10, 최댓값: 100)
    displayArg = 10
    display = "&display={}".format(displayArg)
    # start / Integer / N / 검색 시작 위치(기본값: 1, 최댓값: 1000)
    startArg = 1
    start = "&start={}".format(startArg)
    # sort / String / N / 검색 결과 정렬 방법 /
    # -sim : 정확도순으로 내림차순 정렬(기본값), - date: 날짜순으로 내림차순 정렬
    sortArg = urllib.parse.quote("sim")
    sort = "&sort={}".format(sortArg)
    url = url + display + start + sort
    print("url : {}".format(url))
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    result = json.dumps(response_body.decode('utf-8'), ensure_ascii=False, indent=4)
    res = make_response(result)

    return res