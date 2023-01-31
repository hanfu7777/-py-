from urllib import parse

import requests

url = "https://wxapi.fhd001.com/msapl/print/cancelPackageToDelivery.do"
headers = {"content-type": "application/x-www-form-urlencoded"}
body = {
    'cancelReason': '其它：更新包裹订单',
    'cpCode': 'JD',
    'packageId': 1616719757776283325,
    'referer': 'plwxapi',
    'token': '~XlVWBA0FWlYHURwFSgQVAQUDVQEGDFsLBh1VVQY=~1~'

}
payload = parse.urlencode(body)
response = requests.post(url, headers=headers, data=payload).text
print(response)
