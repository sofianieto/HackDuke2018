from flask import Flask, request
import requests
import random
import mysql.connector
import json

app = Flask(__name__)

with open('configs/configs.json') as json_data:
    jsonInfo = json.load(json_data)
    host = jsonInfo.get("SQLDatabase").get("host")
    user = jsonInfo.get("SQLDatabase").get("user")
    password = jsonInfo.get("SQLDatabase").get("password")

def connectToData():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database="sql9261031"
    )
    return mydb

@app.route('/questionData', methods=['POST'])
def addToData():
    r = request.args
    print(r)
    mydb = connectToData()
    mycursor = mydb.cursor()
    return "0"





    #sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
    #student1 = ("Rachel", 22)
    #mycursor.execute(sqlFormula, student1)  # add formula using given data
    #mydb.commit()  # required to save changes to the table



    # mycursor.execute("SHOW TABLES")
    # for tb in mycursor:
    #     print(tb)

    #mycursor.execute("CREATE TABLE questions (question VARCHAR(500), id INTEGER(20))")


    #mycursor.execute("CREATE DATABASE testdb")
    # mycursor.execute("SHOW DATABASES")
    # for db in mycursor:
    #      print(db)




@app.route("/")
def hello():
    return "Hello World!"






if __name__ == "__main__":
    app.run()
