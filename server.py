from flask import Flask, send_file, Response, send_from_directory
from flask import jsonify,request,render_template
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def mainpage():
    return render_template("./mainContent/index.html")

@app.route("/cover",methods = ["GET","POST"])
def cover():
    return render_template("./cover/index.html")


@app.route("/blog001",methods = ["GET","POST"])
def blog001():
    return render_template("./blog001/index.html")




if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000 ,debug=True)  # 172.20.10.7
    #app.run(host="172.20.10.7",port=5000 ,debug=True) 



