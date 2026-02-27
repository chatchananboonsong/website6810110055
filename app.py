from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

API_URL = "https://countriesnow.space/api/v0.1/countries"

def get_countries_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        json_data = response.json()
        return json_data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/')
def index():
    countries = get_countries_from_api()
    return render_template('index.html', countries=countries)

@app.route('/country/<name>')
def detail(name):
    all_countries = get_countries_from_api()
    # ค้นหาข้อมูลประเทศที่ชื่อตรงกับที่ส่งมา
    country_data = next((item for item in all_countries if item["country"] == name), None)
    
    if country_data is None:
        abort(404)
        
    # แก้ไขชื่อตัวแปรเป็น item เพื่อให้ detail.html ใช้งานได้
    return render_template('detail.html', item=country_data)

if __name__ == '__main__':
    app.run(debug=True)