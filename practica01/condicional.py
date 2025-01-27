from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def home():
    user = {"name":"Juan", "age":30, "is_authenticated": False}
    items = ["pan", "café","cereal", "mermelada"]
    return render_template("condicional.html" ,user=user, items =items)

if __name__=="__main__":
    app.run(debug=True)