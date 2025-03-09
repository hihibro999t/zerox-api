from flask import Flask, Response, request
import json
app = Flask(__name__)

oldmessage = {
    "StatusCode": "Online",
    "PlayersCounts": "nil",
    "JobId": "nil",
}
oldripindra = {
    "StatusCode": "Online",
    "PlayersCounts": "nil",
    "JobId": "nil",
    "Boss Name": "nil"
}
olddoughking = {
    "StatusCode": "Online",
    "PlayersCounts": "nil",
    "JobId": "nil",
    "Boss Name": "nil"
}
@app.route('/api/mirage', methods=["GET", "POST"])
def mirage():
    global oldmessage
    if request.method == "POST":
        oldmessage = request.json
        response_data = json.dumps(
            {
                "message": "Received POST request", 
                "data": oldmessage
            }, separators=(',', ':'))
        return Response(response_data, mimetype='application/json')

    response_data = json.dumps(oldmessage, separators=(',', ':'))
    return Response(response_data, mimetype='application/json')

@app.route('/api', methods=["GET"])
def api():
    return "Hello World!"

@app.route('/api/doughking', methods=["GET", "POST"])
def doughking():
    global olddoughking
    if request.method == "POST":
        olddoughking = request.json
        response_data = json.dumps(
            {
                "message": "Received POST request", 
                "data": olddoughking
            }, separators=(',', ':'))
        return Response(response_data, mimetype='application/json')

    response_data = json.dumps(olddoughking, separators=(',', ':'))
    return Response(response_data, mimetype='application/json')

@app.route('/api/ripindra', methods=["GET", "POST"])
def ripindra():
    global oldripindra
    if request.method == "POST":
        oldripindra = request.json
        response_data = json.dumps(
            {
                "message": "Received POST request", 
                "data": oldripindra
            }, separators=(',', ':'))
        return Response(response_data, mimetype='application/json')

    response_data = json.dumps(oldripindra, separators=(',', ':'))
    return Response(response_data, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
