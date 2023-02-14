from flask import Flask, render_template, request, jsonify, redirect

#Flask, render_template, request, jsonify

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rt4yn64.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


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

    #print(comment_list)

    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
