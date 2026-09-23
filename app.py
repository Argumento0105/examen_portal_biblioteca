from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}


@app.route("/")
def inicio():
    return "Portal de Biblioteca"


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios and usuarios[usuario] == contraseña:
            return "Inicio de sesión correcto"

        else:
            return "Usuario o contraseña incorrectos."

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)