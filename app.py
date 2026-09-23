from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "clave-secreta-portal-biblioteca"

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
            session["usuario"] = usuario
            return redirect(url_for("libros"))

        else:
            return "Usuario o contraseña incorrectos."

    return render_template("login.html")


@app.route("/libros")
def libros():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return "Bienvenido a la biblioteca"


@app.route("/perfil")
def perfil():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return f"Perfil de {session['usuario']}"


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)