from flask import Flask, redirect, render_template, jsonify, make_response, request

import flask

flask.request

import firebase_admin
from firebase_admin import credentials, firestore
import json

import datetime
import threading
from time import sleep

from bson import json_util
# 근무 가능 지역 데이터
import localInfoStatic
# CROS 문제 해결
import flask_cors 

flask_cors.CORS, flask_cors.cross_origin

# 카카오 검색 API
import kakaoSearch
from kakaoSearch import *
# 네이버 검색 API 예제 
from naverSearchApi import *




#Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rt4yn64.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


cred = credentials.Certificate("./bettercoach-d6c79-firebase-adminsdk-gbepe-16fbc97549.json")
firebase_admin.initialize_app(cred)
firebase_db = firestore.client()

# tmPuid = 'RSlQoHFnBOZO3tggCVuh06sjgFJ2'
# collection_uid_member_list = firebase_db.collection(u'member').where(u'uid',u'==', tmPuid).stream()
        
# for doc in collection_uid_member_list:
#     member_object = {}
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

# Create an Event for notifying main thread.
# callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
# def on_snapshot(col_snapshot, changes, read_time):
#     print(u'Callback received query snapshot.')
#     print(u'Current collection_uid_member_list in demo@demo.com')
#     for doc in col_snapshot:
#         print(f'{doc.id}')
#     callback_done.set()

tester_1th = [{'user':"무료체험",'email':"demo@demo.com",'registerDate':"2022. 11. 5.",'lastLogIn':"2022. 11. 17.",'userId':"RSlQoHFnBOZO3tggCVuh06sjgFJ2"}
,{'user':"민이슬",'email':"liseul75@gmail.com",'registerDate':"2022. 11. 5.",'lastLogIn':"2022. 11. 15.",'userId':"29sh0MBTpmVZWGoEZMnmpniCRkm2"}
,{'user':"배민지",'email':"bmg8183@naver.com",'registerDate':"2022. 10. 20.",'lastLogIn':"2022. 11. 7.",'userId':"f89WOu81GNaWDwxJY4EsGYv0RE13"}
,{'user':"신나라",'email':"lljsnrll@naver.com",'registerDate':"2022. 10. 26.",'lastLogIn':"2022. 11. 17.",'userId':"kLN3uMBhCQXlMEMhd4S1BWG9uix1"}
,{'user':"안혜정",'email':"cineclup@naver.com",'registerDate':"2022. 11. 11.",'lastLogIn':"2022. 11. 11.",'userId':"Jl1oxbbjg5Yk1efjoiW7VdF6QU92"}
,{'user':"이준원",'email':"7158ssdl@naver.com",'registerDate':"2022. 10. 24.",'lastLogIn':"2022. 11. 11.",'userId':"7fAzUpmO5fS36b0O0ndNUgn6wZp1"}
,{'user':"한주아",'email':"zua2014@naver.com",'registerDate':"2022. 10. 24.",'lastLogIn':"2022. 11. 16.",'userId':"MeuhoGVGcjhjKlMoyVBryGNzpHK2"}]



# daylesson_list = []
# for docId in member_list:
#     print('docId : '+docId)
#     daylesson_list.append(docId)

# for docId in daylesson_list:
#     collection_doc_id_lesson_note_list = firebase_db.collection(u'daylesson').where(u'docId',u'==', docId).stream()
#     for doc in collection_doc_id_lesson_note_list:
#         print('lessonDate : '+doc.to_dict()['lessonDate'])

# Watch the collection query
# query_watch = collection_uid_member_list.on_snapshot(on_snapshot)

# bettercaoch mongoDB
mongo_client = MongoClient('mongodb+srv://Bettercoachs:BetterCoachs321@cluster0.0xpsm82.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
mongo_db = mongo_client.localInfo



app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mobile')
def mobile():
    return redirect('https://bettercoachs.com')

@app.route('/openchat')
def openchat():
    return render_template('index.html')

@app.route('/insta')
def insta():
    return render_template('index.html')

@app.route('/cafe')
def cafe():
    return render_template('index.html')

@app.route('/tester')
def tester():
    return render_template('index.html')

@app.route('/admin')
def admin():
    tester_1th_val = tester_1th
    return render_template('admin.html', admin_tester_1th_val = tester_1th_val)

@app.route('/getMembersData', methods=["POST"])
def getMembersData():

    member_object_list = []
    
    uidArray_receive = request.form.getlist('uidArray_give')
    for uid in uidArray_receive:
        print("getMembersData uidArray_receive uid : "+uid)
        tmpUid = uid.strip()
        collection_uid_member_list = firebase_db.collection(u'member').where(u'uid',u'==', tmpUid).stream()
        print('getMembersData Before For Statement')
        for doc in collection_uid_member_list:
            member_object = {}
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
            member_object = doc.to_dict()
            member_object['docId'] = doc.id
            member_object_list.append(member_object)

    return jsonify({'member_object_list_give': member_object_list})

@app.route('/getDayLessonsData', methods=["POST"])
def getDayLessonsData():

    daylesson_object_list = []
    
    uidArray_receive = request.form.getlist('uidArray_give')
    startDate = request.form.get('startDate_give',False)
    endDate = request.form.get('endDate_give',False)
    print("startDate : "+startDate)
    print("endDate : "+endDate)
    for uid in uidArray_receive:
        print("getDayLessonsData uidArray_receive uid : "+uid)
        tmpUid = uid.strip()
        collection_daylesson_list = firebase_db.collection(u'daylesson').where(u'uid',u'==', tmpUid).where(u'lessonDate',u'>=',startDate).where(u'lessonDate',u'<=',endDate).stream()
        print('getDayLessonsData Before For Statement')
        for doc in collection_daylesson_list:
            daylesson_object = {}
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
            daylesson_object = doc.to_dict()
            daylesson_object['docUid'] = doc.id
            daylesson_object_list.append(daylesson_object)

    return jsonify({'daylesson_object_list_give': daylesson_object_list})

@app.route('/getLessonNotesData', methods=["POST"])
def getLessonNotesData():

    total_lessonnote_object_list = []
    lessonnote_object_list = []

    jsonData = request.form.get('jsonData')
    print('jsonData : '+jsonData)
    startDate = request.form.get('startDate_give',False)
    endDate = request.form.get('endDate_give',False)
    jsonDict = json.loads(jsonData)
    # print("jsonDict : "+jsonDict[0]['uid'])
    
    print("startDate : "+startDate)
    print("endDate : "+endDate)
    for obj in jsonDict:

        uid = obj['uid']
        docIdList = obj['docIdList']
        daylessonData = obj['daylessonData']
        print("getLessonNotesData uid : "+uid)
        # print("getLessonNotesData docIdList : "+docIdList)
        # print("getLessonNotesData daylessonData : "+daylessonData)

        tmpEditList = []
        tmpDocList = []
        setDocList = list(set(docIdList))
        totalNum = len(setDocList)
        for index in range(len(setDocList)):
            tmpDocList.append(setDocList[index])
            if((index+1)%10 == 0):
                tmpEditList.append(tmpDocList)
                tmpDocList = []
            if(totalNum-1 == index):
                tmpEditList.append(tmpDocList)
        
        for index in range(len(tmpEditList)):
            for idx in range(len(tmpEditList[index])):
                print(u'{}-{}-{}'.format(index,idx,tmpEditList[index][idx]))
        lessonnote_object_list = []
        totalListNum = len(tmpEditList)
        print(u'totalListNum : {}'.format(totalListNum))
        for index in range(len(tmpEditList)):
            print(u'len(tmpEditList[index]) : {}'.format(len(tmpEditList[index])))
            if(len(tmpEditList[index])>0):
                collection_lesson_list = firebase_db.collection(u'lesson').where(u'uid',u'==', uid).where(u'docId',u'in',tmpEditList[index]).where(u'lessonDate',u'>=',startDate).where(u'lessonDate',u'<=',endDate).stream()
                
                print('getLessonNotesData Before For Statement')
                tmpIndex = 0
                for doc in collection_lesson_list:
                    tmpIndex += 1
                    print(u'tmpIndex => {}'.format(tmpIndex))
                    daylesson_object = {}
                    print(u'{} => {}'.format(doc.id, doc.to_dict()['lessonDate']))
                    daylesson_object = doc.to_dict()
                    daylesson_object['docUid'] = doc.id
                    lessonnote_object_list.append(daylesson_object)

            if(totalListNum-1 == index):
                print('last index called!')
                print(u'{} <==> {}'.format(totalListNum-1,index))
                daylesson_object = {}
                daylesson_object['daylessonData'] = daylessonData
                daylesson_object['uid'] = uid
                lessonnote_object_list.append(daylesson_object)
                total_lessonnote_object_list.append(lessonnote_object_list)
                print(u'lessonnote_object_list : {}'.format(lessonnote_object_list))

    return jsonify({'total_lessonnote_object_list_give': total_lessonnote_object_list})

@app.route("/setLocalInfos", methods=["GET"])
def setLocalInfos():
    # sample_receive = request.form['sample_give']

    localInfoList = []
    localInfoList.append(localInfoStatic.seoul)
    localInfoList.append(localInfoStatic.gyeonggi)
    localInfoList.append(localInfoStatic.incheon)
    localInfoList.append(localInfoStatic.gangwondp)
    localInfoList.append(localInfoStatic.daejeon)
    localInfoList.append(localInfoStatic.saejong)
    localInfoList.append(localInfoStatic.chungnam)
    localInfoList.append(localInfoStatic.chungbuk)
    localInfoList.append(localInfoStatic.busan)
    localInfoList.append(localInfoStatic.wulsan)
    localInfoList.append(localInfoStatic.gyungnam)
    localInfoList.append(localInfoStatic.gyungbuk)
    localInfoList.append(localInfoStatic.daegu)
    localInfoList.append(localInfoStatic.gwangju)
    localInfoList.append(localInfoStatic.geonnam)
    localInfoList.append(localInfoStatic.geonbuk)
    localInfoList.append(localInfoStatic.jeju)
    doc = {
        'title': 'localInfoList',
        'info': localInfoList
    }

    print(doc)

    mongo_db.locals.insert_one(doc)

    return jsonify({'msg': '지역정보 저장에 성공하였습니다.'})


@app.route("/getLocalInfos", methods=["GET"])
def getLocalInfos():

    resultObject = list(mongo_db.locals.find({}))

    print(u"resultObject : {}".format(resultObject))

    # 리턴결과 Json 변환
    return json.dumps(resultObject,default=json_util.default)

@app.route("/naverSearch", methods=["GET"])
def naverSearch():
    # 블로그 : blog / 뉴스 : news / 이미지 : image / 지역 : local
    searchType = flask.request.args.get('searchType','blog')
    # URL Params, 그냥 request로 하면 안 되는데, 아마 request 를 불러오는 라이브러리 종류가 달라서 충돌 하는 듯
    queyrString = flask.request.args.get('query','크로스핏') # "크로스핏"
    print("queyrString : {}".format(queyrString))
    
    res = NaverSearch(searchType, queyrString)

    return res
    # return jsonify(response_body.decode('utf-8'))

@app.route("/kakaoSearch", methods=["GET"])
def kakaoSearch():

    query = flask.request.args.get('searchKeyword','카카오')
    print("query : {}".format(query))

    locales = KakaoSearchLocale(query)
    print("locales : {}".format(locales))
    for locale in locales:
        print("locale.pn : {}, locale.x : {}, locale.y : {}".format(locale.pn, locale.x, locale.y))

    return jsonify({'msg': '검색에 성공하였습니다.'},{'result':''})

@app.route("/kakaoMap", methods=["GET"])
def kakaoMap():

    return render_template('basicMap.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    print(doc)

    db.homework.insert_one(doc)

    return jsonify({'msg': '저장에 성공하였습니다.'})


@app.route("/homework", methods=["GET"])
def homework_get():

    comment_list = list(db.homework.find({}, {'_id': False}))


    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
