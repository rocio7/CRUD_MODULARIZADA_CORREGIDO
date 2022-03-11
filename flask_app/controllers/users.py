from flask import Flask, render_template, request, redirect

from flask_app import app
from flask_app.models.users import User
from flask_app.models.classrooms import Classroom
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html", users = users)

@app.route('/new')
def new():
    classrooms = Classroom.muestra_salones()
    return render_template("new.html", classrooms=classrooms)

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.borrar(data)
    return redirect('/')

@app.route ('/edit/<int:id>')
def edit (id):
        data = {
            "id": id
        }
        user = User.mostrar(data)
        classrooms = Classroom.muestra_salones()
        return render_template("edit.html", user=user,classrooms=classrooms )

@app.route('/update', methods=["POST"])
def update():
    User.actualizar(request.form)
    return redirect('/')


@app.route('/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    user = User.mostrar(data)
    return render_template("show.html", user=user)