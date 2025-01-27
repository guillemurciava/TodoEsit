from flask import Flask
app = Flask(__name__)
@app.route("/usuario/<nombre>")
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"
if __name__ == "__main__":
    app.run(debug=True)

# /usuario/Juan devuelve: Hola, Juan!