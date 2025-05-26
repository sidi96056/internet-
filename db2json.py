from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

def export_users_to_json():
    with app.app_context():
        users = User.query.all()
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password  
            })
        
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Kullanıcılar başarıyla users.json dosyasına kaydedildi!")

if __name__ == '__main__':
    export_users_to_json()