from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def home():
    user = {"name":"Juan", "age":30}
    return render_template("index02.html" ,user=user)

if __name__=="__main__":
    app.run(debug=True)