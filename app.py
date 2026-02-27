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

        # 3. ดึงข้อมูลเมืองหลวง
        res_capitals = requests.get("https://countriesnow.space/api/v0.1/countries/capital")
        capitals_data = res_capitals.json().get("data", [])
        capital_map = {item['name']: item['capital'] for item in capitals_data}

        # 4. ดึงข้อมูลพิกัด (Lat/Long)
        res_positions = requests.get("https://countriesnow.space/api/v0.1/countries/positions")
        pos_data = res_positions.json().get("data", [])
        pos_map = {item['name']: {'lat': item['lat'], 'long': item['long']} for item in pos_data}

        # สร้าง Map สำหรับรูปธง
        flag_map = {item['name']: item['flag'] for item in flags_data}
        
        for country in countries_data:
            name = country['country']
            country['flag_url'] = flag_map.get(name, "https://via.placeholder.com/150")
            country['capital'] = capital_map.get(name, "")
            
            # ใส่ค่าพิกัด ถ้าไม่มีให้เป็น 0
            coords = pos_map.get(name, {'lat': 0, 'long': 0})
            country['lat'] = coords['lat']
            country['long'] = coords['long']
            
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

if __name__ == '__main__':
    app.run(debug=True)