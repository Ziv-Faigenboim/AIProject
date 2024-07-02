
from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content="Testing",r=3)
#return "Hello! this is the main page <h1>Hello<h1>"
#changedsfsadfgsdfgsdffgs
#@app.route("/<name>")
#def user(name):
 #   return f"hello {name}!"

#@app.route("/admin")
#def admin():
 #   return redirect(url_for("user",name="Admin!"))

if __name__ == "__main__":
    app.run()
