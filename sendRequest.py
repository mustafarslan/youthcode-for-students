import requests
import json


def calculate():
    return {"groupId": 2, "questionNum": 3, "result": 7}


def send_answer(data):
    url = 'http://localhost:5000/api/answer'
    r = requests.post(url, data=json.dumps(data))
    print(r)


if __name__ == '__main__':
    result = calculate()
    send_answer(result)
