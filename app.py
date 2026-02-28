from flask import Flask, render_template, abort, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy 
import requests
import os
from dotenv import load_dotenv # นำเข้า load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

app = Flask(__name__)

# ดึงค่า Secret Key และ Database URL จาก .env
app.secret_key = os.getenv('FLASK_SECRET_KEY') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app)

# สร้าง Model ผู้ใช้
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# สร้างฐานข้อมูลและ User เริ่มต้น
with app.app_context():
    db.create_all()
    if not User.query.filter_by(email='admin@gmail.com').first():
        db.session.add(User(email='admin@gmail.com', password='1234'))
        db.session.commit()

# --- 2. ฟังก์ชันดึงข้อมูล API (ต้องมีไว้เหมือนเดิม) ---
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

# --- 3. Routes ---

@app.route('/')
def index():
    countries = get_combined_data()
    return render_template('index.html', countries=countries)

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
        
        # ค้นหาจาก Database (ลบ load_users ออกไปแล้ว)
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:
            session['user'] = user.email
            return redirect(url_for('index'))
        return "Login Failed! อีเมลหรือรหัสผ่านไม่ถูกต้อง"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/settings')
def settings():
    if 'user' not in session: 
        return redirect(url_for('login'))
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)