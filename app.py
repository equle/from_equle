from flask import Flask, request, render_template, redirect, url_for, session
import game
import json
import sqlite3
import defdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

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

    elif data == 'signpage':
            return render_template('sign.html')
    
    elif data == 'chapter1':
        character = game.get_charact()
        return render_template('chapter1.html', data = character)

    elif data == 'chapter1.1':
        character = game.get_charact()
        return render_template('chapter1.1.html', data = character)

    elif data == 'chapter1.2':
        character = game.get_charact()
        return render_template('chapter1.2.html', data = character)
    
    elif data == 'chapter2':
        character = game.get_charact()
        return render_template('chapter2.html', data = character)
    
    elif data == 'chapter2.1':
        character = game.get_charact()
        return render_template('chapter2.1.html', data = character)
    
    elif data == 'chapter2.2':
        character = game.get_charact()
        return render_template('chapter2.2.html', data = character)

    else :
        return render_template('index.html')


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        id = request.form["id"]
        pw = request.form["pw"]
        defdb.insert_data(id, pw)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(id, pw)

@app.route('/getinfo')
def getinfo():
    info = defdb.select_all()
    return render_template("info.html", data=info)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        if id == 'abc' and pw == '1234':
            session['user'] = id
            return '''
                <script> alert("안녕하세요~ {}님");
                location.href="/form"
                </script>
            '''.format(id)
            return redirect(url_for('form'))
        else:
            return "아이디 또는 패스워드를 확인 하세요."


# session 제거 로그아웃
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

# 로그인할 수 있는 사용자만 접근 가능
@app.route('/form')
def form():
    if 'user' in session:
        return render_template('game.html')
    return redirect(url_for('login'))

# save file

# @app.route('/getinfo')
# def getinfo():
#     # 파일 입력
#     with open("static/save.txt", "r", encoding='utf-8') as file:
#         student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
#     return '이름 : {}, 번호 : {}'.format(student[0], student[1])

# send data to gameintro.html


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


@app.route('/getname', methods=['GET','POST'])
def gamesave():
    username = request.form['user']
    game.set_charact(username)
    character = game.get_charact()
    return render_template('gameintro.html', data = character)


## app.run ##
if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for('daum'))
    app.run(debug=True)