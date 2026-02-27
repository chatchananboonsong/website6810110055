from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

def get_combined_data():
    try:
        # 1. ดึงข้อมูลชื่อประเทศและเมือง
        res_countries = requests.get("https://countriesnow.space/api/v0.1/countries")
        countries_data = res_countries.json().get("data", [])

        # 2. ดึงข้อมูลรูปธงชาติ
        res_flags = requests.get("https://countriesnow.space/api/v0.1/countries/flag/images")
        flags_data = res_flags.json().get("data", [])

        # 3. นำรูปมาใส่ในข้อมูลหลัก โดยใช้ชื่อประเทศเป็นตัวเชื่อม
        # สร้าง Dictionary เพื่อให้ค้นหารูปได้เร็วขึ้น
        flag_map = {item['name']: item['flag'] for item in flags_data}
        
        for country in countries_data:
            # เอารูปจาก flag_map มาใส่ ถ้าไม่มีให้ใส่รูปว่างๆ ไว้
            country['flag_url'] = flag_map.get(country['country'], "https://via.placeholder.com/150")
            
        return countries_data
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    countries = get_combined_data()
    return render_template('index.html', countries=countries)

@app.route('/country/<name>')
def detail(name):
    all_countries = get_combined_data()
    country = next((item for item in all_countries if item["country"] == name), None)
    if not country:
        abort(404)
    return render_template('detail.html', country=country)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)