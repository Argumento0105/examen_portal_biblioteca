from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)

app.secret_key = "clave-secreta-portal-biblioteca"


# Usuarios
usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}


# Libros
lista_libros = [
    {
        "titulo": "Python desde cero",
        "autor": "Juan Pérez",
        "disponibles": 4
    },
    {
        "titulo": "Desarrollo Web",
        "autor": "María López",
        "disponibles": 2
    },
    {
        "titulo": "Inteligencia Artificial",
        "autor": "Pedro García",
        "disponibles": 0
    }
]


# Inicio
@app.route("/")
def inicio():

    mensaje = session.pop("mensaje", None)

    return render_template(
        "index.html",
        mensaje=mensaje
    )


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios and usuarios[usuario] == contraseña:

            session["usuario"] = usuario

            respuesta = make_response(
                redirect(url_for("libros"))
            )

            respuesta.set_cookie(
                "ultimo_usuario",
                usuario
            )

            return respuesta

        return render_template(
            "login.html",
            error="Usuario o contraseña incorrectos."
        )

    return render_template("login.html")


# Libros
@app.route("/libros")
def libros():

    usuario = session.get("usuario")

    return render_template(
        "libros.html",
        libros=lista_libros,
        usuario=usuario
    )


# Perfil
@app.route("/perfil")
def perfil():

    if "usuario" not in session:
        return redirect(url_for("login"))

    usuario = session["usuario"]

    return render_template(
        "perfil.html",
        usuario=usuario
    )


# Eliminar cookie
@app.route("/eliminar-cookie")
def eliminar_cookie():

    respuesta = make_response(
        redirect(url_for("inicio"))
    )

    respuesta.delete_cookie("ultimo_usuario")

    return respuesta


# Cerrar sesión
@app.route("/logout")
def logout():

    session.clear()

    session["mensaje"] = "La sesión fue cerrada correctamente."

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)