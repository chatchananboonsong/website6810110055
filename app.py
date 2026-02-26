from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # ข้อมูลตัวละคร 20 ตัว (ลบ URL รูปภาพออก)
    countries = [
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
        {"name": "Agnes Tachyon", "capital": "アグネスタキオン", "continent": "Leader"},
        {"name": "Manhattan Cafe", "capital": "マンハッタンカフェ", "continent": "Betweener"},
        {"name": "Kitasan Black", "capital": "キタサンブラック", "continent": "Runner"},
        {"name": "Satono Diamond", "capital": "サトノダイヤモンド", "continent": "Leader"}
    ]
    return render_template('index.html', countries=countries)

if __name__ == '__main__':
    app.run(debug=True)