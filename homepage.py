from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def deafult():
   return ("falsk response")

@app.route("/ntfy")
def ntfy():
   return "ToDO"
if __name__=="__main__":
    app.run()