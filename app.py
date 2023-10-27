from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Nao Nao Bro"

@app.route("/play")
@app.route("/play/")
@app.route("/play/<int:num>")
def playint(num=3):
    return render_template("index.html", num=num)

@app.route("/play/<int:num>/")
@app.route("/play/<int:num>/<string:colorc>")
def playintstring(num=3, colorc=""):
    return render_template("index.html", num=num, colorc=colorc)

if __name__=="__main__":
    app.run(debug=True)