from flask import Flask
from pytz import timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def raretech_message():
    return '夢は、目標に向かって毎日歩みを進めた者だけが叶えられる。\
            今日の二時間は、その一歩だ'

@app.route('/time', methods=['GET'])
def current_time():
    tz = timezone('Japan')
    jst_time = datetime.now(tz).strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{jst_time}です'

if __name__ == '__main__':
    app.run()
