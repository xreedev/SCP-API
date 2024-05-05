import json,time
file="test.txt"
dict_a={}

with open(file) as f:
    for line in f:
        scp_id,scp_name=line.strip().split(None,1)
        dict_a[scp_id]=scp_name.strip()
outfile=open("test3.json","w")
json.dump(dict_a, outfile, indent = 4, sort_keys = False)
outfile.close()
from flask import *

app=Flask(__name__)
@app.route('/',methods=['GET'])
def myfunc():
    with open('test3.json') as test1:
     dataset=json.load(test1)
     datasetjson=json.dumps(dataset)
    return datasetjson
app.run(port=7775)




