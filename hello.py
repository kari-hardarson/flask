from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html",head="Haus",body=range(10))

@app.route("/help")
def hjalp():
    return "<h1>Hjalp</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/doit",methods=["GET","POST"])
def doit():
    #print request.args["lastname"]
    lastname=request.form["lastname"]
    return "Done"+lastname

@app.route("/dothat/<a>/<b>")
def dothat(a,b):
    print a,b
    return "Done"

if __name__ == "__main__":
    app.run(debug=True)
