import json
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:AlEx1902345@localhost/web_db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"


data = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['GET'])
def get():
    info = Users.query.order_by(Users.id).all()
    data.clear()
    for el in info:
        dict_json = {'id': el.id, 'name': el.name, 'surname': el.surname}
        data.append(dict_json)
    articles = jsonify(data)
    return render_template("json_users.html", articles=data)


@app.route('/users/user', methods=['GET'])
def get1():
    info = Users.query.order_by(Users.id).all()
    data.clear()
    for el in info:
        dict_json = {'id': el.id, 'name': el.name, 'surname': el.surname}
        data.append(dict_json)
    articles = jsonify(data)
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add():
    name = request.json['name']
    surname = request.json['surname']
    user = Users(name=name, surname=surname)
    with app.app_context():
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    articles = jsonify(data)
    return render_template("json_users.html", articles=data)



@app.route('/users', methods=['DELETE'])
def delete():
    id_delete = Users.query.get_or_404(int(request.json['id']))
    try:
        db.session.delete(id_delete)
        db.session.commit()
        articles = jsonify(data)
        return render_template("json_users.html", articles=data)
    except:
        return "При удалении пользователя произошла ошибка"


@app.route('/users', methods=['PUT'])
def update():
    id_put = Users.query.get_or_404(int(request.json['id']))
    if request.json['name']:
        id_put.name = request.json['name']
    if request.json['surname']:
        id_put.surname = request.json['surname']
    try:
        db.session.commit()
        articles = jsonify(data)
        return render_template("json_users.html", articles=data)
    except:
        return "При обновлении пользователя произошла ошибка"
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)