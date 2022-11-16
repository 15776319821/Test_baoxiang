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
        params = {'uid': '2005', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJNakF3TlE9PSIsInh5eiI6IlFURXdOMFE0TWtJdE0wVkROaTAwTWpVeExUazFOVGt0TmtRNU9FSTVRVVExTjBOQyIsImV4cCI6MTkyNDQwMDA0OX0.--fH2wg9y64EOIfATAIxb1wAuQMPOS6wzMnfaejb4Pg'}
        number=10
        for i in range(number):
            result = requests.post(url=hots+url+'uid='+uid+'&token='+token, data=json.dumps(data), headers=headers).json()
            # res = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
            logger.info(result)
            # print(res)
            giftId = (jsonpath.jsonpath(result, '$.data.toPersonGiftInfos[*].giftInfo.giftId'))
            serverTime = (jsonpath.jsonpath(result, '$.serverTime'))
            giftId = giftId+serverTime
            RunMain().set_csv(giftId)
            print(giftId)