from flask import *
import json,time

app=Flask(__name__)
@app.route('/',methods=['GET'])
def myfunc():
    with open('test1.json') as test1:
     dataset=json.load(test1)
     datasetjson=json.dumps(dataset)
    return datasetjson
app.run(port=7777)
