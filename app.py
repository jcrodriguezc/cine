from flask import Flask, render_template as render

app = Flask(__name__)

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

@app.route("/template", methods= ["GET"])
def template():
    return render ("template.html")

if __name__=="__main__":
    app.run(debug=True)
