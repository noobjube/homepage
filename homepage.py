from flask import Flask,render_template,redirect,url_for,request
import os,re

app = Flask(__name__)

@app.route("/")
def deafult():
   return ("falsk response")

@app.route("/ntfy",methods=["POST"])
def ntfy():
   if request.method == "POST":
      text = request.form['ntfy text']
      os.system('curl -d "'+text+'" http://home.pi:8081/PiAlerts')
   return redirect("http://home.pi:8081")
if __name__=="__main__":
    app.run(debug = True,host='0.0.0.0',port=5000)