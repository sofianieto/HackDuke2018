from flask import Flask
import requests
import random
import mysql.connector
import json

#app = Flask(__name__)
with open('configs/configs.json') as json_data:
    jsonInfo = json.load(json_data)
    host = jsonInfo.get("SQLDatabase").get("host")
    user = jsonInfo.get("SQLDatabase").get("user")
    password = jsonInfo.get("SQLDatabase").get("password")

def connectToData():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    mycursor = mydb.cursor()
    #sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
    #student1 = ("Rachel", 22)
    #mycursor.execute(sqlFormula, student1)  # add formula using given data
    #mydb.commit()  # required to save changes to the table



    # mycursor.execute("SHOW TABLES")
    # for tb in mycursor:
    #     print(tb)

    #mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


    #mycursor.execute("CREATE DATABASE testdb")
    # mycursor.execute("SHOW DATABASES")
    # for db in mycursor:
    #     print(db)




#@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    print(connectToData())
    #app.run()
