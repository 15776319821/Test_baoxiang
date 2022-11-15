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

    def send_post(self, url, data, headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data, headers=headers).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) #json转字符串
        return result

    def send_get(self, url, data ,headers):
        result = requests.get(url=url, data=data ,headers=headers)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) #json转字符串
        return result

    def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        headers = {
        "version": "1.9.0",
        "accept": "*/*",
        "fid": "0",
        "Content-Type": "application/json",
        "shumeiid": "AsssBT",
        "os": "2",
        "accept-language": "zh-Hans-CN;q=1, ar-CN;q=0.9, en-CN;q=0.8, zh-Hant-CN;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "deviceid": "A107D82B-3EC6-4251-9559-6D98B9AD57CB",
        "user-agent": "Pocket/1.9.0 (iPhone; iOS 14.8.1; Scale/3.00)",
        "lang": "zh_CN",
        "distinctid": "E71038ED-F200-4BE7-95AE-CA8CF92392EE_31",
        "model": "iPhone_X_14.8.1"
    }
        # time.sleep(5)

        if method == 'post':
            result = self.send_post(url, data, headers)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data, headers)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    hots = 'https://dev.api.koudailive.com'
    url = '/api/trade/gift/giveGiftsBaoxiang?'
    uid = '2005'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNakF3TlE9PSIsInh5eiI6IlFURXdOMFE0TWtJdE0wVkROaTAwTWpVeExUazFOVGt0TmtRNU9FSTVRVVExTjBOQyIsImV4cCI6MTkyNDQwMDA0OX0.--fH2wg9y64EOIfATAIxb1wAuQMPOS6wzMnfaejb4Pg'
    data = {
        "roomId": 100455,
        "count": 1,
        "source": 0,
        "toUserIds": [1813],
        "giftId": 43016
    }
    params = {'uid': '2005', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNakF3TlE9PSIsInh5eiI6IlFURXdOMFE0TWtJdE0wVkROaTAwTWpVeExUazFOVGt0TmtRNU9FSTVRVVExTjBOQyIsImV4cCI6MTkyNDQwMDA0OX0.--fH2wg9y64EOIfATAIxb1wAuQMPOS6wzMnfaejb4Pg'}


    # results = requests.post(url=hots+url, data=json.dumps(data), headers = headers, params= params).json()
    # res = json.dumps(results, ensure_ascii=False, sort_keys=True, indent=2)
    result = RunMain().run_main('post', hots+url+'uid='+uid+'&token='+token, json.dumps(data))
    # login_res = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    # title=['zhuangbei','time']
    with open(log_path+"/pocket.csv", "a+", newline='', encoding='utf-8') as w_file:
        writer = csv.writer(w_file)
        # 写入标题
        # writer.writeheader()
        # 将数据写入
        giftId = (jsonpath.jsonpath(result, '$.data.toPersonGiftInfos[*].giftInfo.giftId'))
        serverTime = (jsonpath.jsonpath(result, '$.serverTime'))
        giftId = giftId+serverTime
        print(giftId)
        writer.writerow(giftId)
        w_file.close()



