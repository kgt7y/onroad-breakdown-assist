from flask import Flask, render_template, flash, request, session
import pickle

import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def DoctorLogin():
    return render_template('AdminLogin.html')


@app.route("/NewEmployee")
def NewEmployee():
    return render_template('NewEmployee.html')


@app.route("/EmployeeLogin")
def EmployeeLogin():
    return render_template('EmployeeLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewProduct")
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AEmployeeInfo")
def AEmployeeInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeetb  ")
    data = cur.fetchall()
    return render_template('AEmployeeInfo.html', data=data)


@app.route("/APaymentInfo")
def APaymentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='Waiting For Payment'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM booktb where Status ='Paid'    ")
    data2 = cur.fetchall()
    return render_template('APaymentInfo.html', data1=data1, data2=data2)


@app.route("/AbookingInfo")
def AbookingInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='waiting'    ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where (Status ='Approved' or Status ='Reject')  ")
    data2 = cur.fetchall()

    return render_template('AbookingInfo.html', data1=data1, data2=data2)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/newemp", methods=['GET', 'POST'])
def newemp():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']
        city = request.form['city']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employeetb VALUES ('','" + name + "','" + gender + "','" +   mobile+ "','" +  email+ "','" + address + "','" + uname + "','" + password + "','" + city + "')")
        conn.commit()
        conn.close()
        flash('Employee Info Register Successfully')
        return render_template('NewEmployee.html')


@app.route("/emplogin", methods=['GET', 'POST'])
def emplogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['ename'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from employeetb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('EmployeeLogin.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM employeetb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('EmployeeHome.html', data=data)


@app.route("/EmployeeHome")
def EmployeeHome():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeetb where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('EmployeeHome.html', data=data)


@app.route("/profile")
def profile():
    id = request.args.get('id')
    session['eid'] = id
    return render_template('ProfileUpdate.html')


@app.route("/updatepro", methods=['GET', 'POST'])
def updatepro():
    if request.method == 'POST':
        mobile = request.form['mobile']
        email = request.form['email']
        username = session['ename']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute(
            "Update   employeetb set mobile='" + mobile + "',email='" + email + "' where id ='" + session['eid'] + "'")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM employeetb where username='" + username + "' ")
        data = cur.fetchall()

        flash("Profile Update  successfully")

        return render_template('EmployeeHome.html', data=data)


@app.route("/EBookInfo")
def EBookInfo():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='waiting' And EmpName='" + username + "'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where (Status ='Approved' or Status ='Reject') And EmpName='" + username + "'  ")
    data2 = cur.fetchall()

    return render_template('EBookInfo.html', data1=data1, data2=data2)


@app.route("/Approved")
def Approved():
    id = request.args.get('lid')
    username = session['ename']
    mob = request.args.get('mob')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cursor = conn.cursor()
    cursor.execute("Update booktb set Status='Approved'  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='waiting' And EmpName='" + username + "'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where (Status ='Approved' or Status ='Reject') And EmpName='" + username + "'  ")
    data2 = cur.fetchall()

    return render_template('EBookInfo.html', data1=data1, data2=data2)


@app.route("/Reject")
def Reject():
    id = request.args.get('lid')
    username = session['ename']
    mob = request.args.get('mob')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cursor = conn.cursor()
    cursor.execute("Update booktb set Status='Reject'  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='waiting' And EmpName='" + username + "'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where (Status ='Approved' or Status ='Reject')  And EmpName='" + username + "'  ")
    data2 = cur.fetchall()

    return render_template('EBookInfo.html', data1=data1, data2=data2)


@app.route("/amt")
def amt():
    bid = request.args.get('lid')
    st = request.args.get('st')
    session['bid'] = bid
    if st == "Reject":
        flash('Request Reject')
        return render_template('EBookInfo.html')
    else:
        return render_template('EPayment.html')


@app.route("/updateamt", methods=['GET', 'POST'])
def updateamt():
    if request.method == 'POST':
        amt = request.form['amt']
        username = session['ename']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute(
            "Update   booktb set Status='Waiting For Payment',Amount='" + str(amt) + "' where id ='" + str(
                session['bid']) + "'")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM booktb where Status='Waiting For Payment' And EmpName='" + username + "'   ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM booktb where Status ='Paid'  And EmpName='" + username + "'  ")
        data2 = cur.fetchall()
        flash("Amount Update  successfully")

        return render_template('EPaymentInfo.html', data1=data1, data2=data2)


@app.route("/EPaymentInfo")
def EPaymentInfo():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='Waiting For Payment' And EmpName='" + username + "'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM booktb where Status ='Paid'  And EmpName='" + username + "'  ")
    data2 = cur.fetchall()
    return render_template('EPaymentInfo.html', data1=data1, data2=data2)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        import re

        def solve(s):
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(pat, s):
                return True
            return False

        print(solve(email))

        if solve(email):
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + gender + "','" +  mobile + "','" +  email+ "','" + address + "','" + uname + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('User Register successfully')
            return render_template('UserLogin.html')

        else:
            flash('Email Id Incorrect')
            return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:
            session['mob'] = data[3]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/UEmployeeInfo")
def UEmployeeInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Employeetb   ")
    data = cur.fetchall()
    return render_template('UEmployeeInfo.html', data=data)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        city = request.form['city']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  Employeetb  where city='" + city + "'  ")
        data = cur.fetchall()
        return render_template('UEmployeeInfo.html', data=data)


@app.route("/book")
def Book():
    eid = request.args.get('id')
    session['eid'] = eid
    uname = session['uname']

    return render_template('UBook.html',uname =uname )


@app.route("/empbook", methods=['GET', 'POST'])
def empbook():
    if request.method == 'POST':
        uname = session['uname']
        vtype = request.form['vtype']
        vno = request.form['vno']
        lmark = request.form['lmark']
        address = request.form['address']
        Fault = request.form['Fault']
        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from employeetb where id ='" + str(session['eid']) + "' ")
        data = cursor.fetchone()
        if data:
            ename = data[6]
            mobile = data[3]
            Email = data[4]
            print(ename)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO  booktb VALUES ('','" + uname + "','" + session[
                    'mob'] + "','" + vtype + "','" + vno + "','" + lmark + "','" + address
                + "','" + Fault + "','" + savename + "','" + ename + "','" + mobile + "','" + Email + "','waiting','','" + date + "')")
            conn.commit()
            conn.close()
        flash('Employee Booked successfully')
        return render_template('UBook.html')


@app.route("/UserBookInfo")
def UserBookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where UserName='" + uname + "' and Status='waiting' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "' and  Status='Approved' or Status='Reject' ")
    data2 = cur.fetchall()

    return render_template('UserBookInfo.html', data1=data1, data2=data2)


@app.route("/UserPaymentInfo")
def UserPaymentInfo():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where Status='Waiting For Payment' And Username='" + uname + "'   ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM booktb where Status ='Paid'  And USerName='" + uname + "'  ")
    data2 = cur.fetchall()
    return render_template('UserPaymentInfo.html', data1=data1, data2=data2)


@app.route("/payment")
def payment():
    bid = request.args.get('lid')
    amt = request.args.get('amt')
    session["bid"] = bid

    return render_template('UPayment.html', amt=amt)


@app.route("/upayment", methods=['GET', 'POST'])
def upayment():
    if request.method == 'POST':
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cursor = conn.cursor()
        cursor.execute(
            "update booktb set Status ='Paid' where id='" + session[
                'bid'] + "' ")
        conn.commit()
        conn.close()

        flash('Amount Paid  Successfully')
        uname = session['uname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM booktb where Status='Waiting For Payment' And Username='" + uname + "'   ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2breakingdowndb')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM booktb where Status ='Paid'  And USerName='" + uname + "'  ")
        data2 = cur.fetchall()
        return render_template('UserPaymentInfo.html', data1=data1, data2=data2)


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


def sendmsg(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "sampletest685@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "hneucvnontsuwgpj")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
