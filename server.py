from flask import Flask, send_file, Response, send_from_directory
from flask import jsonify,request,render_template
app = Flask(__name__)
deploy_port =  "http://114.55.178.110"#"http://192.168.43.185" #"http://114.55.178.110" #阿里云"http://114.55.178.110" #


@app.route("/cover",methods = ["GET","POST"])
def cover():
    global deploy_port
    kwargs = {
        "deploy_port": deploy_port
    }    
    return render_template("./cover/index.html",**kwargs)


@app.route("/",methods = ["GET","POST"])
def mainpage():
    global deploy_port
    kwargs = {
        "deploy_port": deploy_port
    }
    return render_template("./mainContent/index.html",**kwargs)

@app.route("/<blogindex>",methods = ["GET","POST"])
def blogs(blogindex):
    global deploy_port
    kwargs = {
        "deploy_port": deploy_port
    }
    return render_template("./blogs/{}/index.html".format(blogindex),**kwargs)

@app.route("/ar",methods = ["GET","POST"])
def ar():
    global deploy_port
    kwargs = {
        "deploy_port": deploy_port
    }
    return render_template("./love_2.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000 ,debug=True)  # 172.20.10.7
    #app.run(host="172.20.10.7",port=5000 ,debug=True) 



