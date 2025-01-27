from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/formulario", methods=["GET", "POST"])
def manejar_formulario():
    if request.method == "POST":
        datos = request.form["nombre"]
        return f"Recibido: {datos}"
    return '''
        <form method="post">
        Nombre: <input type="text" name="nombre">
        <input type="submit">
        </form>
        '''
if __name__ == "__main__":
    app.run(debug=True)