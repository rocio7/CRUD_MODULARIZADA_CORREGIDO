from flask import Flask, render_template, request, redirect

from flask_app import app
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html",users=users)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.guardar(request.form)
    return redirect('/')