import requests
import json
import jsonpath
import time
import csv
from common.Log import logger
import getpathInfo
import os
from datetime import datetime
now = datetime.now()
path = getpathInfo.get_Path()
log_path = os.path.join(path, 'result')  # 存放log文件的路径
formatted_date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

logger = logger
class RunMain():

    def send_post(self, url, data, headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        try:
            res = requests.post(url=url, data=data, headers=headers, timeout=(3, 20))  # 因为这里要封装post方法，所以这里的url和data值不能写死
            print("请求相应时间"+str(res.elapsed.total_seconds()))
        except requests.exceptions.RequestException as e:
            print("Error 服务异常")
            print(e)
            return None
        else:
            return res.json()


    def send_get(self, url, data ,headers):
        try:
            result = requests.get(url=url, data=data, headers=headers, timeout=(3, 10))
            # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) #json转字符串
        except:
            print("Error 服务异常")
            return {'code': '服务502'}
        else:
            return result

    def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        headers = {
            "deviceId": "420368AB-EE9A-46DE-AF81-54622A8E8517",
            "lang": "zh_CN",
            "version": "1.13.0",
            "os": "1",
            "model": "M2012K10C",
            "buyUser": "0",
            "advertisingId": "2118bc0e-1917-4c06-b830-b1dcacba8c1b",
            "appsFlyerId": "1686636899650-6983902825347051450",
            "distinctId": "420368AB-EE9A-46DE-AF81-54622A8E8517_23",
            "fid": "20001",
            "shumeiId": "BnwMLwJPg9Ycv3TLRzbQYiWk8lW6xoaOTn9iVKuMeOeXJrzoU9AxDuf+JK+H2sylvKCD2qY+jxPRkRQwQfYII5g==",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "59",
            "Host": "54.169.197.10",
            "Accept-Encoding": "gzip",
            "User-Agent": "Layla/1.12.2 (iPhone; iOS 16.3.1; Scale/3.00)",
            "Connection": "keep-alive"
        }
        # time.sleep(5)

        if method == 'post':
            result = self.send_post(url, data, headers)
            # logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data, headers)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result

    def set_csv(self, data =None):
        with open(log_path + "/luckGift_"+str(formatted_date_time)+".csv", "a+", newline='', encoding='utf-8') as w_file:
            try:
                writer = csv.writer(w_file)
                # 写入标题
                # writer.writeheader()
                # 将数据写入
                try:
                    writer.writerow(data)
                finally:
                    w_file.close()
            except IOError as IOError:
                print(IOError)
                print("Error: 写入文件异常")



if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    hots = 'https://dev.laylachat.com'
    url = '/api/trade/gift/giveGifts?'
    uid = '791980'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJOemt4T1RndyIsInh5eiI6Ik5ESXdNelk0UVVJdFJVVTVRUzAwTmtSRkxVRkdPREV0TlRRMk1qSkJPRVU0TlRFMyIsImV4cCI6MTk2NDc2NTc4M30.CrQXoDPBxrZ5cgsnJVi-6vqvjNBEejQOyg8SysoFKPQ'
    data = {
        "callId": "",
        "roomId": 101071,
        "count": 1,
        "source": 0,
        "toUserIds": [791980],
        "giftId": 49001
    }
    # params = {'uid': '2005', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNakF3TlE9PSIsInh5eiI6IlFURXdOMFE0TWtJdE0wVkROaTAwTWpVeExUazFOVGt0TmtRNU9FSTVRVVExTjBOQyIsImV4cCI6MTkyNDQwMDA0OX0.--fH2wg9y64EOIfATAIxb1wAuQMPOS6wzMnfaejb4Pg'}

    number = 10000
    for i in range(number):
        result = RunMain().run_main('post', hots+url+'uid='+uid+'&token='+token, json.dumps(data))
        if (result != None):
            try:
                luckyGiftDiamondCount = (jsonpath.jsonpath(result, '$.data.toUserInfo[0].luckyGiftDiamondCount'))
                giftId = (jsonpath.jsonpath(result, '$.data.giftInfo.giftId'))
                serverTime = (jsonpath.jsonpath(result, '$.serverTime'))
            except TypeError as TypeError:
                print(TypeError)
                print('服务异常：'+str(result))
                logger.info(result)
                time.sleep(200)
            else:
                giftIds = giftId + luckyGiftDiamondCount + serverTime
                RunMain().set_csv(giftIds)
                print(i)







