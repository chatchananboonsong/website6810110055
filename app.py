from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    characters = [
        {"name": "Jin Kazama", "style": "Karate", "origin": "Japan", "img": "https://images.tcdn.com.br/img/img_prod/730030/estatua_jin_kazama_tekken_7_pure_arts_7995_1_20200812163459.jpg"},
        {"name": "Kazuya Mishima", "style": "Mishima Karate", "origin": "Japan", "img": "https://m.media-amazon.com/images/I/5162-Lh-4KL._AC_UF894,1000_QL80_.jpg"},
        {"name": "King", "style": "Pro Wrestling", "origin": "Mexico", "img": "https://m.media-amazon.com/images/I/61M6X6X8z1L._AC_SL1200_.jpg"},
        {"name": "Paul Phoenix", "style": "Judo / Karate", "origin": "USA", "img": "https://m.media-amazon.com/images/I/61TstY7-WpL._AC_SL1200_.jpg"},
        {"name": "Hwoarang", "style": "Taekwondo", "origin": "Korea", "img": "https://m.media-amazon.com/images/I/61Vv8A6pMFL._AC_SL1500_.jpg"},
        {"name": "Ling Xiaoyu", "style": "Chinese Martial Arts", "origin": "China", "img": "https://m.media-amazon.com/images/I/61D6TBy9+iL._AC_SL1000_.jpg"},
        {"name": "Nina Williams", "style": "Assassination Arts", "origin": "Ireland", "img": "https://m.media-amazon.com/images/I/61o3N6oV+hL._AC_SL1200_.jpg"},
        {"name": "Marshall Law", "style": "Jeet Kune Do", "origin": "USA", "img": "https://m.media-amazon.com/images/I/61P0S6oV+hL._AC_SL1200_.jpg"},
        {"name": "Yoshimitsu", "style": "Ninjutsu", "origin": "Japan", "img": "https://m.media-amazon.com/images/I/71R1S6oV+hL._AC_SL1500_.jpg"},
        {"name": "Reina", "style": "Mishima Karate", "origin": "Japan", "img": "https://m.media-amazon.com/images/I/61K0S6oV+hL._AC_SL1200_.jpg"}
    ]
    return render_template('index.html', characters=characters)

if __name__ == '__main__':
    app.run(debug=True)