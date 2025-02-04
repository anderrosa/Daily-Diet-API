from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql=pymysql://user:admin123@127.0.0.1:3306/daily_diet'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)