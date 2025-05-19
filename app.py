from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)

db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "root",
    "database" : "atm"
}
@app.route("/")
def landing():
    return render_template("home.html")

@app.route("/withdraw1")
def withdraw1():
    return render_template("withdraw1.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/withdraw2",methods=["POST","GET"])
def withdraw2():
    accno = request.form["account_number"]
    pin = request.form["pin"]
    
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("withdraw1.html",msg="noaccount")
    elif data[-2] is None:
        return render_template("withdraw1.html",msg="nopin")
    elif data[-2] != int(pin):
        return render_template("withdraw1.html",msg="wrongpin")
    else:
        return render_template("withdraw2.html",user_name=data[1],accno=accno)
@app.route("/withdraw3",methods=["POST","GET"])
def withdraw3():
    accno = request.form["accno"]
    amount = request.form["amount"]

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT USER_BALANCE,USER_NAME FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)

    if int(amount) <= int(data[0]):
        balance = int(data[0]) - int(amount)
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_BALANCE = %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(balance,accno))
        conn.commit()
        conn.close()
        return render_template("withdraw2.html",msg="balance",accno=accno,user_name=data[1])
    else:
        return render_template("withdraw2.html",msg="nobalance",accno=accno,user_name=data[1])

@app.route("/deposit1")
def deposit1():
    return render_template("deposit1.html")

@app.route("/deposit2",methods=["POST","GET"])
def deposit2():
    accno = request.form["accno"]
    amount = int(request.form["amount"])

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("deposit1.html",msg="noaccount")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_BALANCE = USER_BALANCE + %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(amount,accno))
        conn.commit()
        conn.close()
        return render_template("deposit1.html",msg = "account" )

@app.route("/ministatement1")
def ministatement1():
    return render_template("ministatement1.html")
@app.route("/ministatement2",methods=["POST","GET"])
def ministatement2():
    accno = request.form["accno"]
    pin = request.form["pin"]

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("ministatement1.html",msg="noaccount")
    elif data[-2] is None:
        return render_template("ministatement1.html",msg="nopin")
    elif int(pin) != int(data[-2]):
        return render_template("ministatement1.html",msg="wrongpin")
    else:
        name = data[0]
        email = data[1]
        balance = data[-1]
        return render_template("ministatement2.html",accno=accno,name=name,email=email,balance=balance)
@app.route("/pingeneration1")
def pingeneration1():
    return render_template("pingeneration1.html")
@app.route("/pingeneration2",methods=["POST","GET"])
def pingeneration2():
    accno = request.form["accno"]

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM ACCOUNTS WHERE USER_ACCNO = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("pingeneration1.html",msg="noaccount")
    elif data[-2] != None:
        return render_template("pingeneration1.html",msg="account")
    else:
        return render_template("pingeneration2.html",accno=accno)
@app.route("/pingeneration3",methods=["POST","GET"])
def pingeneration3():
    accno = request.form["accno"]
    pin = request.form["pin"]
    cpin = request.form["cpin"]
    if pin != cpin:
        return render_template("pingeneration2.html",accno=accno,msg="wrongpin")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "UPDATE ACCOUNTS SET USER_PIN = %s WHERE USER_ACCNO = %s"
        cursor.execute(query,(pin,accno))
        conn.commit()
        conn.close()
        return render_template("pingeneration2.html",msg="ok")
app.run(port=5016)

