from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
sql_data = {
    "host" : "localhost",
    "user" : "root",
    "passwd" : "p9tc1OTJ65:w",
    "db" : "testdb",
    "charset" : "utf8",
    "port" : 3306
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':

        conn = pymysql.connect(**sql_data)
        coursor = conn.cursor()
        coursor.execute("SELECT username, password FROM user WHERE username = %s", (request.form['Name']))
        data = coursor.fetchall()
        coursor.close()
        conn.close()

        if request.form['Password'] == data[0]["password"]:
            return render_template("result.html")
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/search',methods = ['POST'])
def search():
    if request.method == 'POST':
        
        conn = pymysql.connect(**sql_data)
        coursor = conn.cursor()


        if request.form['IP']:
            coursor.execute("SELECT Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN FROM testdata WHERE SourceIP = %s ORDER BY usec ASC", (request.form['IP']))
            data = coursor.fetchall()
            return render_template("search.html", data=data)
        elif request.form['TM']:
            coursor.execute("SELECT Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN FROM testdata WHERE usec = %s ORDER BY usec ASC", (request.form['TM']))
            data = coursor.fetchall()
            return render_template('search.html', data=data)
        elif request.form['FQ']:
            coursor.execute("SELECT Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN FROM testdata WHERE FQDN = %s ORDER BY usec ASC", (request.form['FQ']))
            data = coursor.fetchall()
            return render_template('search.html', data=data)

        coursor.close()
        conn.close()
    else:
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
