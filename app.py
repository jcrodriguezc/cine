from flask import Flask, render_template as render
from db import get_db

app = Flask(__name__)

tipoUsuarios = ["usuario","administrador","superadministrador"]

@app.route("/", methods= ["GET"])
def inicio():
    return render ("index.html")

@app.route("/registro", methods= ["GET","POST"])
def registro():
    return render ("registro.html")

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
    
    if tipoUsuario in tipoUsuarios:
        if tipoUsuario == "usuario":
            return render ("usuario.html")        
        else:
            return render ("dashboard.html")
    else:
        return f"Error: El usuario no existe"

if __name__=="__main__":
    app.run(debug=True)
