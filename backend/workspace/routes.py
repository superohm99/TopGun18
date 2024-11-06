from flask import Flask,jsonify, request
from workspace import app,collection
from datetime import datetime
from pydantic import BaseModel

class Alert(BaseModel):
    failureType: str
    status: bool
    createDate: datetime

@app.route('/')
def index():
    return "<h1>Hello </h1>"

def saveData():
    return

def getDataMqtt():
    return

@app.route('/sendData',methods=["GET"])
def sendData():
    data = {"key1":"data1","key2":"data2"}
    return  jsonify(data),200

@app.route('/createData',methods=["POST"])
def createData():
    alertData = request.json
    alertData['createDate'] = datetime.today()
    alert = Alert(**alertData)
    result = collection.insert_one(alert.dict())
        
    return {
        "id" : str(result.inserted_id),
        "failureType" : str(alert.failureType),
        "status": bool(alert.status),
        "createDate": str(alert.createDate)
    },201
