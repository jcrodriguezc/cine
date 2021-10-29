from os import error
from flask import Flask, url_for,redirect, render_template as render
import sqlite3
from sqlite3 import Error

from werkzeug.utils import redirect
from db import get_db
from flask import request

app = Flask(__name__)

@app.route("/", methods= ["GET"])
def inicio():
    return render ("index.html")

@app.route("/registro", methods= ["GET","POST"])
def registro():    
    return render("registro.html")

@app.route("/registro_usuario", methods= ["POST"])
def registro_usuario():
    if request.method =="POST":
        tipoUsuario="usuario"
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        clave = request.form["clave"]
        db = get_db()        
        db.executescript ("INSERT INTO usuarios (tipoUsuario, nombre, correo, clave) VALUES ('%s','%s','%s','%s')"%("usuario",nombre,correo,clave))
        db.commit()     
        db.close()
        return render("index.html")

@app.route("/ingreso_usuario", methods=["POST"])
def ingreso_usuario():
    if request.method == "POST":        
        correo_ingreso = request.form["correo_ingreso"]
        clave_ingreso = request.form["clave_ingreso"]
        tipousuario="usuario"
        print(correo_ingreso,clave_ingreso)
        db=get_db()        
        usuario = db.execute('SELECT * FROM usuarios WHERE correo=? AND clave=?',(correo_ingreso,clave_ingreso))        
        if usuario:
            administrador = "juan@gmail.com"
            superadministrador = "norvey@gmail.com"
            if correo_ingreso==administrador or correo_ingreso == superadministrador:
                return render("dashboard.html")
            else:
                return render("usuario.html")
        else:
            return render("registro.html")


@app.route("/dashboard", methods= ["GET","POST"])
def dashboard():
    return render ("dashboard.html")

@app.route("/busqueda", methods= ["GET","POST"])
def busqueda():
    return render("busqueda.html")

@app.route("/pelicula", methods= ["GET"])
def pelicula():
    return render ("pelicula.html")

@app.route("/usuario/<tipoUsuario>", methods= ["GET","POST"])
def tipoUsuario(tipoUsuario):
    
    # if tipoUsuario in tipoUsuarios:
    #     if tipoUsuario == "usuario":
    #         return render ("usuario.html")        
    #     else:
    #         return render ("dashboard.html")
    # else:
        return "Error: El usuario no existe"

if __name__=="__main__":
    app.run(debug=True)
