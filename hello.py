from flask import Flask, escape, request, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
# 서버만들고 서버 실행
# def함수는 함수를 선언할 때 사용

@app.route('/myname')
def myname():
    return '차하연입니다'
    # 서버를 나오기 위해 ctrl+c
    # /는 어디로 갈지를 루트 역할
    # myname에서 ()는 입력값없이 실행만하면 특정값 출력됨

# 랜덤으로 점심메뉴를 추천해주는 서버
@app.route('/lunch')
def lunch():
    menu = ['양자강', '김밥카페', '20층','순남시래기']
    lunch = random.choice(menu)
    return lunch
    # 이제 이 코드를 lunch()한줄로 표현가능


# 아이돌 백과사전
@app.route('/idol')
def idol():
    idols = {
        'bts':{
            '지민' :25,
            '랩몬스터' :23
        },
        'rv':'레드벨벳',
        '핑클' : {
            '이효리' : '거꾸로해도이효리',
            '옥주현' : '35'
        },
        'SES' : ['유진','바다','슈']
    }
    return idols
# json viewer chrome 을 설치해야 우리언어로 표시됨(key값은 진하게, value는 보통으로 출력)
# 딕셔너리안 딕셔너리, 배열 가능

@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트', '1번 포스트', '2번 포스트']
    return posts[num]

# 실습 cube뒤에 전달될 수의 세제곱수를 화면에 보여주세요
# 1 -> 1
# 2 -> 8
# str() : 숫자를 문자로 바꿔주는 함수
@app.route('/cube/<int:num>')
def cube(num):
    cubes = num*num*num
    return str(cubes)


# 클라이언트에게 html 파일을 주고싶어요!
@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    # age = request.args['age']
    return render_template('pong.html', age_in_html=age)

# 로또 번호 가져와서 보여주는 서버(회차 적을 시 결과 출력)
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}'))

    winner.append(result.get('bnusNo'))

    return json.dumps(winner)


app.run(debug=True)
# 코드를 저장하면 ctrl+c안해도 디버깅해주는 역할
