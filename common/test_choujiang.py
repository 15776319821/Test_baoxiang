import requests
import json
import jsonpath
import time
import csv
from common.Log import logger
import getpathInfo
import os
path = getpathInfo.get_Path()
log_path = os.path.join(path, 'result')  # 存放log文件的路径
logger = logger

class RunMain():
    def set_csv(self, data=None):
        with open(log_path + "/pocket.csv", "a+", newline='', encoding='utf-8') as w_file:
            writer = csv.writer(w_file)
            # 写入标题
            # writer.writeheader()
            # 将数据写入
            writer.writerow(data)
            w_file.close()


if __name__ == '__main__':
        hots = 'http://dev.laylachat.com'
        url = '/api/trade/ld/drew?'
        uid = '790761'
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJOemt3TnpZeCIsInh5eiI6Ik5UbGxPV0k0WlRVeVlqY3dOR1U0TUdGaE5ERXhZVFkxWVRNMFltWXpORFU9IiwiZXhwIjoxOTQ1NzM4MTcyfQ.xlS7CZbEiIzRJ2rWI8c1dfUAAl4_MdhHif-Xxk2gpiw'
        # data = {
        #     "roomId": 100455,
        #     "count": 1,
        #     "source": 0,
        #     "toUserIds": [1813],
        #     "giftId": 43016
        # }
        headers = {
            "deviceId": "59e9b8e52b704e80aa411a65a34bf345",
            "lang": "es_ES",
            "cc":"cn" ,
            "version": "1.1.0",
            "os": "1",
            "model": "SM-G973U1",
            "buyUser": "0",
            "advertisingId": "9f230806-fecc-46dc-af59-fd1020923449",
            "appsFlyerId": "1685934141372-7242749009515216363",
            "distinctId": "baaf472a-9e20-4e81-b56e-f083daf155a2",
            "fid": "2001",
            "shumeiId": "BpwrPGqhX1huTkNZeYOIYrZEe30tgE8/Zu/cm4arxxW/gFE0DszuQTcEwPVQmqz4gK58AFx0jNn9pdZ3rTsLf/g==",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "117",
            "Host": "dev.laylachat.com",
            "Accept-Encoding": "gzip",
            "Cookie": "JSESSIONID=04C7FB63A69D6C2B82B2905186307DBC",
            "User-Agent": "okhttp/3.12.13",
            "Connection": "keep-alive"
        }
        # params = {'uid': '2005', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNakF3TlE9PSIsInh5eiI6IlFURXdOMFE0TWtJdE0wVkROaTAwTWpVeExUazFOVGt0TmtRNU9FSTVRVVExTjBOQyIsImV4cCI6MTkyNDQwMDA0OX0.--fH2wg9y64EOIfATAIxb1wAuQMPOS6wzMnfaejb4Pg'}
        number=10000
        for i in range(number):
            result = requests.get(url=hots+url+'uid='+uid+'&token='+token, headers=headers).json()
            # result = requests.get(url='https://dev.api.koudailive.com/api/trade/ld/drew?uid=2595&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNalU1TWc9PSIsInh5eiI6IlJrRXhNRGRDUlRVdE5UQTROeTAwTURBM0xUaEZORU10TXpCRE1qZzRSREUyT1VGRSIsImV4cCI6MTkyNzk3MTYwNn0.q7bfSjoERnelGHfg8CTaI15GdOWj7Hz5DNfcr6K8xkk', headers=headers).json()
            # res = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
            logger.info(result)
            giftId = (jsonpath.jsonpath(result, '$.data.goodsId'))
            serverTime = (jsonpath.jsonpath(result, '$.serverTime'))
            # print(giftId)
            # print(serverTime)
            giftId = giftId+serverTime
            RunMain().set_csv(giftId)
            # print(giftId)
            print(i)