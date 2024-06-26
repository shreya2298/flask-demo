from flask import Flask, request
from getdata import fetch_all_rows_as_dict
import mysql.connector
import math
from dbconnect import insert_data

app = Flask(__name__)
conn = mysql.connector.connect(
    host="192.168.1.2", user="root", password="shreya", database="flaskdb"
)
cursor = conn.cursor()


# PATH PARAMETERS
@app.route("/sqr/<num>")
def square(num):
    return str(float(num) * float(num))


@app.route("/sqrroot/<num>")
def square_root(num):
    result = math.sqrt(float(num))
    return f"{result}"


@app.route("/user/<num>")
def getuser(num):
    result = fetch_all_rows_as_dict(num)
    return f"{result}"



# QUERY PARAMETERSs
@app.route("/cube")
def data():
    # here we want to get the value of num (i.e. ?num=some-number)
    num = float(request.args.get("num"))
    cube = num * num * num
    return f"{cube}"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    return insert_data(values=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
