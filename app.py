from flask import Flask, request, jsonify
from models.user import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily_diet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/Meal", methods=['POST'])
def create_meals():
    return "Minha primeira refeiçao"

if __name__ == '__main__':
    app.run(debug=True)