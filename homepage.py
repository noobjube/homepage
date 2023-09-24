from flask import Flask,render_template,redirect,url_for,request
import os,re
from urllib.parse import urlparse

app = Flask(__name__)

global hostname

@app.route("/host",methods=["POST"])
def deafult():
   global hostname
   hostname = "http://"+urlparse(request.base_url).hostname+"/"
   return redirect(hostname)

@app.route("/ntfy",methods=["POST"])
def ntfy():
   if request.method == "POST":
      text = request.form['ntfy text']
      os.system('curl -d "'+text+'" http://home.pi:8081/PiAlerts')
   return redirect(hostname)

@app.route("/wakepc")
def wakepc():
   os.system('sudo etherwake 50:eb:f6:9f:f8:53')
   return redirect(hostname)


if __name__=="__main__":
    app.run(debug = True,host='0.0.0.0',port=5000)