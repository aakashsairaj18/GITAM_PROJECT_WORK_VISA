import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import smtplib
from email.message import EmailMessage

flask_app = Flask(__name__, template_folder='E:/_01/final deploy/deploying')

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/model")
def model():
    return render_template("model.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    model = pickle.load(open("flask_model01.pkl", "rb"))
    pos = [x for x in request.form.values()]
    print(pos)
    # pos[0],pos[11]=pos[11],pos[0]
    # pos[1],pos[10]=pos[10],pos[1]
    if pos[7]=="":
        pos[7]=0
    if pos[6]=="No":
        pos[6]=0
    else:
        pos[6]=1

    print(pos)
    float_features=['1','1','1','1','1','109116.8','1','1','2015','1','India']
    #print(float_features)
    del float_features[-1]
    #print(float_features)
    float_features=[float(x) for x in float_features]
    #print(float_features)
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if pos[6]==0:
        full="No"
    else:
        full="Yes"

    subject="Here are your results of Visa Analysis"
    body="Dear "+pos[0]+",\nDetails:\nName:"+pos[0]+"\nEmployer Name:"+pos[2]+"\nSOC Name: "+pos[3]+"\nSOC Code: "+pos[4]+"\nJob Title: "+pos[5]+"\nFull time: "+full+"\nWage: "+str(pos[7])+"\nCity: "+pos[8]+"\nState: "+pos[9]+"\nYear: "+pos[10]+"\nCountry of Origin: "+pos[11]+"\nYour chance of getting visa is "
    #Email Alerts

    if int(pos[6])==0:
        body+="Lower"
    elif float(pos[7])<=60000:
        body+="Lower"
    elif prediction==1:
        body+="Higher"
    else:
        body+="Higher"
    body+="\n"
    body+="\nFrom Team Wisa, GITAM"
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=pos[1]

    user="workvisa.gitam@gmail.com"
    msg['from']=user
    password="zoglcpbkamwqtwld"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()




    if int(pos[6])==0:
        return render_template("op_low.html", prediction_text = "The chances of getting H1B is low",ans0=pos[2],ans1=pos[3],ans2=pos[4],ans3=pos[5],ans4=full,ans5=pos[7],
                               ans6=pos[8],ans7=pos[9],ans8=pos[10],ans9=pos[-1],ans10=pos[1],ans11=pos[0])
    elif float(pos[7])<=60000:
        return render_template("op_low.html", prediction_text = "The chances of getting H1B is low",ans0=pos[2],ans1=pos[3],ans2=pos[4],ans3=pos[5],ans4=full,ans5=pos[7],
                               ans6=pos[8],ans7=pos[9],ans8=pos[10],ans9=pos[-1],ans10=pos[1],ans11=pos[0])
    elif prediction==1:
        return render_template("op_high.html", prediction_text = "The chances of getting H1B is Higher",ans0=pos[2],ans1=pos[3],ans2=pos[4],ans3=pos[5],ans4=full,ans5=pos[7],
                               ans6=pos[8],ans7=pos[9],ans8=pos[10],ans9=pos[-1],ans10=pos[1],ans11=pos[0])
    else:
        return render_template("op_low.html", prediction_text = "The chances of getting H1B is Low",ans0=pos[2],ans1=pos[3],ans2=pos[4],ans3=pos[5],ans4=full,ans5=pos[7],
                               ans6=pos[8],ans7=pos[9],ans8=pos[10],ans9=pos[-1],ans10=pos[1],ans11=pos[0])



if __name__ == "__main__":
    flask_app.run(debug=True)