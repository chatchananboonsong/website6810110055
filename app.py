from flask import Flask, render_template, abort, request, redirect, url_for, session
import requests
import json
import os

app = Flask(__name__)
app.secret_key = 'dev_key_12345' # รหัสลับสำหรับระบบ Login
USER_FILE = 'users.json'

def load_users():
    if not os.path.exists(USER_FILE):
        # สร้างไฟล์เริ่มต้นถ้ายังไม่มี
        with open(USER_FILE, 'w') as f: json.dump({"admin@mail.com": "1234"}, f)
    with open(USER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_combined_data():
    try:
        res_countries = requests.get("https://countriesnow.space/api/v0.1/countries")
        countries_data = res_countries.json().get("data", [])
        res_flags = requests.get("https://countriesnow.space/api/v0.1/countries/flag/images")
        flags_data = res_flags.json().get("data", [])
        flag_map = {item['name']: item['flag'] for item in flags_data}
        for country in countries_data:
            country['flag_url'] = flag_map.get(country['country'], "https://via.placeholder.com/150")
        return countries_data
    except: return []

@app.route('/')
def index():
    countries = get_combined_data()
    return render_template('index.html', countries=countries)

# --- แก้ไขบั๊ก: เพิ่ม Route 'detail' ที่หายไป ---
@app.route('/country/<name>')
def detail(name):
    all_countries = get_combined_data()
    country = next((item for item in all_countries if item["country"] == name), None)
    if not country: abort(404)
    return render_template('detail.html', country=country)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        users = load_users()
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('index'))
        return "Login Failed!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/settings')
def settings():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)