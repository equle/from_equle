from flask import Flask, request, render_template, redirect, url_for
import game
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/hello/')
# def hello():
#     return 'Hello, World'

#page move

@app.route('/<string:data>')
def movepage(data):
    if data == 'loginpage':
        return render_template('login.html')

    elif data == 'gamepage':
            return render_template('game.html')

    else :
        return render_template('index.html')


#'login'

@app.route('/putinfo', methods=['GET','POST'])
def putinfo():
    ID = request.form['ID']
    PW = request.form['PW']
    if request.method == 'GET':
        return "GET으로 보내진 데이터는 보호되지 않습니다 전달된 데이터({},{})".format(ID, PW)
    else :
        with open("static/save.txt","w",encoding='utf-8') as f:
            f.write("%s,%s" % (ID, PW))
        return redirect(url_for('getinfo'))

# save file

@app.route('/getinfo')
def getinfo():
    # 파일 입력
    with open("static/save.txt", "r", encoding='utf-8') as file:
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
    return '이름 : {}, 번호 : {}'.format(student[0], student[1])

# send data to gameintro.html
@app.route('/getname', methods=['GET','POST'])
def gamesave():
    username = request.form['user']
    game.set_charact(username)
    character = game.get_charact()
    return render_template('gameintro.html', character = character)

## method
# @app.route('/method',  methods=['GET', 'POST'])
# def method():
#     if request.method == 'GET':
#         return 'GET으로 전송한다.'
#     else :
#         num = request.form['num']
#         name = request.form['name']
#         printdata = 'POST로 전달된 학번은 {}이고 이름은 {}이다.)'.format(num, name)
#         return printdata

## URL
## URL_FOR
# @app.route('/naver')
# def daum():
#     return redirect("https://www.daum.net/")
#      return render_template('naver.html')

# # @app.route('/move/<name>')
# # def movevar(name):
# #     if name == 'naver':
# #         return redirect(url_for('naver'))
# #     elif name == 'daum':
# #         return redirect(url_for('daum'))
# #     else :
# #         return redirect(url_for('index'))



## app.run ##
if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for('daum'))
    app.run(debug=True)