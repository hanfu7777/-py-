from urllib import parse

import requests

null = ""
false = False
true = True
url = "https://wxapi.fhd001.com/msapl/print/savePackageToDelivery.do"
headers = {"content-type": "application/x-www-form-urlencoded"}
body = {
    "changeWlb": 1,
    "consigneeList": [
        {"consigneeName": "zzc", "consigneeMobile": "18864669221", "consigneePhone": "", "consigneeProvince": "浙江省",
         "consigneeCity": "杭州市", "consigneeArea": "滨江区", "consigneeTown": "",
         "consigneeAddress": "青集社科创园a308", "consigneeZip": "", "consigneeId": 126939149}],
    "shippingName": "句号",
    "shippingMobile": 18658054864,
    "shippingProvince": "浙江省",
    "shippingCity": "杭州市",
    "shippingArea": "富阳区",
    "shippingAddress": "银湖科技城53栋",
    "id": 31471569,
    "isDefault": "OPEN",
    "idAuthStatus": "NO",
    "initials": "J",
    "nameInitials": "JH",
    "updateTime": 1670225980,
    "packageCategory": "服饰",
    "packagePostfee": 10,
    "packageWeight": 1,
    "createUser": {"userId": 77978412, "encryptUserId": null, "userNick": "0", "dbNo": 6,
                   "avatar": "https://oss.fhd001.com/fhdowx/avatarIamge/6642029d35744309894975e8e8e02c6c.jpg",
                   "phoneNumber": "18658054864", "deliverStatus": null, "netpointId": 0, "cpCode": null,
                   "netpointCode": null, "netpointName": null, "extensionCode": null, "expert": null, "member": null,
                   "group": null, "idAuthStatus": "NO", "appId": null, "shareFromNeedAuth": null,
                   "userRole": "PERSONAL", "groupAdminUserKey": null, "subUserNick": null, "timestamp": 1667896298,
                   "fhdCode": "1r89t4", "userType": null, "first": false, "corpId": null, "ip": null, "groupId": 0,
                   "teamRole": false, "groupAdminUserId": 0, "groupAdmin": false, "seedExpert": false,
                   "targetUserId": 77978412, "targetUserNick": "0", "targetUserDbNo": 6, "pddOrderDbNo": 6,
                   "youzanOrderDbNo": 6, "deliver": false, "uc": "a570aGtuYm1jbW1p"},
    "userId": 77978412,
    "createUserId": 77978412,
    "userNick": 0,
    "title": "服饰",
    "param": {"expressType": 1, "timeType": 2, "version": 1, "noLossWorry": true, "newExpress": true, "riskArea": false,
              "totalOriginPrice": 10, "receiveTime": "2022-12-27 22:00"},
    "cpCode": "JD",
    "source": "fhdq",
    "expressType": "undefined",
    "sendStartTime": '1672081113',
    "sendEndTime": '1672082113',
    "token": "~XlVWBA0FWlYHURwFSgQVAQUDVQEGDFsLBh1VVQY=~1~",
    "referer": "plwxapi",
    "barCode": null,
    "companyName": null,
    "packageFlag": null,
    "packageId": null,
    "packageNote": null,
    "packageValume": null,
    "shareUserId": null,
    "shippingCompany": null,
    "shippingPhone": null,
    "shippingShopName": null,
    "shippingZip": null,
    "templateId": null,
    "tradeMemo": null,
}
payload = parse.urlencode(body, doseq=True)
# print(payload)
response = requests.post(url=url, headers=headers, data=payload).json()
print(response)
