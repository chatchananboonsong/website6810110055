from flask import Flask, render_template, abort

app = Flask(__name__)

# ดึงข้อมูลออกมาไว้ข้างนอกเพื่อให้ทุก Route เรียกใช้ได้
countries_data = [
        {"name": "Special Week", "capital": "スペーシャルウィーク", "continent": "Leader"},
        {"name": "Silence Suzuka", "capital": "サイレンススズカ", "continent": "Runner"},
        {"name": "Tokai Teio", "capital": "トウカイテイオー", "continent": "Leader"},
        {"name": "Maruzensky", "capital": "マルゼンスキー", "continent": "Runner"},
        {"name": "Fuji Kiseki", "capital": "フジキセキ", "continent": "Leader"},
        {"name": "Oguri Cap", "capital": "オグリキャップ", "continent": "Betweener"},
        {"name": "Gold Ship", "capital": "ゴールドシップ", "continent": "Chaser"},
        {"name": "Vodka", "capital": "ウオッカ", "continent": "Betweener"},
        {"name": "Daiwa Scarlet", "capital": "ダイワスカーレット", "continent": "Runner"},
        {"name": "Taiki Shuttle", "capital": "タイキシャトル", "continent": "Leader"},
        {"name": "Grass Wonder", "capital": "グラスワンダー", "continent": "Betweener"},
        {"name": "Hishi Amazon", "capital": "ヒシアマゾン", "continent": "Chaser"},
        {"name": "Mejiro McQueen", "capital": "メジロマックイーン", "continent": "Leader"},
        {"name": "El Condor Pasa", "capital": "エルコンドルパサー", "continent": "Leader"},
        {"name": "Symboli Rudolf", "capital": "シンボリルドルフ", "continent": "Leader"},
        {"name": "Rice Shower", "capital": "ライスシャワー", "continent": "Betweener"},
        {"name": "Agnes Tachyon", "capital": "アグネスタキอน", "continent": "Leader"},
        {"name": "Manhattan Cafe", "capital": "マンハッタンカフェ", "continent": "Betweener"},
        {"name": "Kitasan Black", "capital": "キタサンブラック", "continent": "Runner"},
        {"name": "Satono Diamond", "capital": "サトノダイヤモンド", "continent": "Leader"}
]

@app.route('/')
def index():
    return render_template('index.html', countries=countries_data)

# Route ใหม่สำหรับหน้ารายละเอียด
@app.route('/character/<name>')
def detail(name):
    # ค้นหาข้อมูลตัวละครที่ชื่อตรงกับที่ส่งมา
    character = next((item for item in countries_data if item["name"] == name), None)
    if character is None:
        abort(404)  # ถ้าไม่เจอชื่อ ให้ส่ง Error 404
    return render_template('detail.html', character=character)

if __name__ == '__main__':
    app.run(debug=True)