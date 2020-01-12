from flask import Flask, request , redirect, render_template , url_for
from fractions import Fraction
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    if request.method=="POST":
        operand=request.form['operand']

        if operand in ['add','+','ADD','sum','SUM'] :
            q = redirect("http://127.0.0.1:5000/add")

        elif operand in ['sub','-','SUB','difference','DIFFERENCE']  :
            q = redirect("http://127.0.0.1:5000/sub")

        elif operand in ['multiply','mul','MUL','product','PRODUCT','*']:
            q = redirect("http://127.0.0.1:5000/mul")

        elif operand in ['div','DIV','/','divide','DIVIDE'] :
            q = redirect("http://127.0.0.1:5000/div")
        elif operand in ['=','&','|','>','<','%','!']:
            q = redirect("http://127.0.0.1:5000/error")
        else :
            q = print('error')
        return q

    return render_template("intro.html")

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method=="POST":
        Q=request.form['firstnumber']
        W=request.form['lastnumber']
        a=Fraction(Q)
        b=Fraction(W)
        E=(a)+(b)
        R=str(E).split('/')
        if len(R) == 2:
            T=int(R[0])/int(R[1])
            Y=str(T).split(".")
            if Y[1] == '0':
                return "Your result is %s\n" % Y[0]
            else:
                return  "Your result is %s\n" %T
        else:
            U=str(E).split(".")
            return "Your result is %s \n" % U[0]

    return render_template("home.html")

@app.route('/sub',methods=["GET","POST"])
def sub():
    if request.method=="POST":
        Q=request.form['firstnumber']
        W=request.form['lastnumber']
        a=Fraction(Q)
        b=Fraction(W)
        E=(a)-(b)
        R=str(E).split('/')
        if len(R) == 2:
            T=int(R[0])/int(R[1])
            Y=str(T).split(".")
            if Y[1] == '0':
                return "Your result is %s\n" % Y[0]
            else:
                return  "Your result is %s\n" %T
        else:
            U=str(E).split(".")
            return "Your result is %s \n" % U[0]

    return render_template("home.html")

@app.route('/mul',methods=["GET","POST"])
def mul():
    if request.method=="POST":
        Q=request.form['firstnumber']
        W=request.form['lastnumber']
        a=Fraction(Q)
        b=Fraction(W)
        E=(a)*(b)
        R=str(E).split('/')
        if len(R) == 2:
            T=int(R[0])/int(R[1])
            Y=str(T).split(".")
            if Y[1] == '0':
                return "Your result is %s\n" % Y[0]
            else:
                return  "Your result is %s\n" %T
        else:
            U=str(E).split(".")
            return "Your result is %s \n" % U[0]

    return render_template("home.html")

@app.route('/div',methods=["GET","POST"])
def div():
    if request.method=="POST":
        Q=request.form['firstnumber']
        W=request.form['lastnumber']
        a=Fraction(Q)
        b=Fraction(W)
        E=(a)/(b)
        R=str(E).split('/')
        if len(R) == 2:
            T=int(R[0])/int(R[1])
            Y=str(T).split(".")
            if Y[1] == '0':
                return "Your result is %s\n" % Y[0]
            else:
                return  "Your result is %s\n" %T
        else:
            U=str(E).split(".")
            return "Your result is %s \n" % U[0]

    return render_template("home.html")
@app.route('/error',methods=["GET","POST"])
def error():
    return render_template("error.html")
if __name__ == '__main__':
   app.run(debug = True)