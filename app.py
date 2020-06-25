from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/hello')
# def hello():
#     return render_template("hello.html")

@app.route('/hello/<name>')
def hello(name):
    return "hello {}".format(name)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        num = request.args["num"]
        # name = request.args["name"]
        # num = request.args.get("num")
        name = request.args.get("name")
        # num = request.form["num"]
        # name = request.form["name"]
        return "GET으로 전달({},{})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        # num = request.args["num"]
        # name = request.args.get("name")
        
        return "POST로 전달({},{})".format(num, name)

@app.route('/test')
def test1():
    return 'test1'

@app.route('/test/')
def test2():
    return 'test2'

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/nopage')
def nopage ():
    print("404로 보냅니다.")
    abort(404)
    return "404로 보냅니다."

@app.route('/pang')
def pang ():
    return render_template("pg.html")

if __name__ =='__main__':
    with app.test_request_context():
        print(url_for('daum'))

    app.run(debug=True)
