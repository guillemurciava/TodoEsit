from flask import Flask
app = Flask(__name__)
@app.route("/producto/<int:id>")
def mostrar_producto(id):
    return f"Mostrando producto con ID: {id}"
if __name__ == "__main__":
    app.run(debug=True)

# /producto/42 devuelve: Mostrando producto con ID: 42