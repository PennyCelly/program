import requests
import base64
import json
import sys

if len(sys.argv) != 3:
    print("输入参数不合法，使用方法： python forbidFsp.py name ip \n如：python forbidFsp.py FRC.XHY 10.11.6.29:9990")
    sys.exit()

# python3 forbidFsp.py FMC.FMA.CutActivityController.newAxesTaskList 10.11.48.21:8082
# 要禁用的fspName
name = sys.argv[1]
# 要禁用的ip
ip = sys.argv[2]


def post(url, params):
    encode = str(base64.b64encode(json.dumps(params).encode('utf-8')),'utf-8')
    res = requests.post(url, json=encode)
    res = str(base64.b64decode(res.text), 'utf-8')
    return json.loads(res)


def get(url, params):
    encode = str(base64.b64encode(json.dumps(params).encode('utf-8')),'utf-8')
    res = requests.get(url+"?"+encode)
    res = str(base64.b64decode(res.text), 'utf-8')
    return json.loads(res)

queryUrl = "http://api.fsp.fbs.sit.blackfi.sh:10249/fsp/register/service/query"
forbidUrl = "http://api.fsp.fbs.sit.blackfi.sh:10249/fsp/register/provider/config"
params = {
    "name": name,
    "start": 0,
    "limit": 1000
}

res = get(queryUrl, params)
for item in res["data"]["rows"]:
    params = {
        "name": item["name"],
        "providerAddress": ip,
        "forbidOper": 2
    }
    res = post(forbidUrl, params)
    if res["success"]:
        print("禁用成功", item["name"])
    else:
        print("禁用失败", item["name"])