from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/refeicao", methods=['GET'])
def meals():
    return "Minha primeira refeição!"

if __name__ == '__main__':
    app.run(debug=True)