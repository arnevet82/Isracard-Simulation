import requests
import json


class Verification():
    def __init__(self):
        self.BASE_URL = 'https://stdigital.isracard.co.il/services/ProxyRequestHandler.ashx?reqName='
        self.HEADERS = {
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'content-type': 'application/x-www-form-urlencoded',
    }

    def verify_account(self, business_num, account_num):
        url = self.BASE_URL + 'FlexIdentifyMarchant'
        payload = {
            "supplierId": str(business_num),
            "accountNo": str(account_num)
        }
        response = requests.post(url=url, headers=self.HEADERS, data=payload)
        content = json.loads(response.content)
        if 'FlexIdentifyMarchantBean' in content:
            output = content['FlexIdentifyMarchantBean']['message']
        else:
            output = content['Header']['Message']

        return output

    def verify_id(self, user_id):
        url = self.BASE_URL + 'IdentifySalesAttendant'
        payload = {
            "tzDayal": str(user_id),
            "kodPeula": 1,
            "kvutzatShiuch": 327
        }

        response = requests.post(url=url, headers=self.HEADERS, data=payload)
        content = json.loads(response.content)
        if 'IdentifySalesAttendantBean' in content:
            output = content['IdentifySalesAttendantBean']['message']
        else:
            output = content['Header']['Message']

        return output

