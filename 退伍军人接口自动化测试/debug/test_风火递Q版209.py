import os
import re

if os.name == 'nt':
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
else:
    hosts_path = '/etc/hosts'


class HostsUtils(object):
    @staticmethod
    def getHostsData():
        try:
            with open(hosts_path, 'r+') as f:
                data = f.read()
                f.close()
            return data
        except PermissionError as e:
            raise ('读取hosts文件失败,', e)

    @staticmethod
    def setHostsData(data: str = '', mode: str = 'w'):
        data = data.strip()
        re_ip_str = re.search('(\d|\.)+', data).group()
        print('ip:', re_ip_str)
        re_domain_str = re.search('[a-zA-z0-9|\.]+[a-zA-Z]+$', data).group()
        print('domain:', re_domain_str)
        if 3 != re_ip_str.count('.') or \
                int(re_ip_str.split('.')[0]) not in range(256) or \
                int(re_ip_str.split('.')[1]) not in range(256) or \
                int(re_ip_str.split('.')[2]) not in range(256) or \
                int(re_ip_str.split('.')[3]) not in range(256) or \
                re_ip_str.startswith('.') or \
                re_ip_str.endswith('.'):
            raise ValueError('您输入的IP地址是无效值！')
        elif 0 == re_domain_str.count('.') or \
                re_domain_str.startswith('.') or \
                re_domain_str.endswith('.'):
            raise ValueError('您输入的域名是无效值！')
        else:
            try:
                with open(hosts_path, mode) as f:
                    f.write(data)
                    f.close()
            except PermissionError as e:
                raise ('因为无权访问所以失败！', e)


data209 = '''
192.168.16.10 common.fhd001.com
192.168.16.10 wxapi.fhd001.com
192.168.16.10 fhdowx.xyy001.com
192.168.16.10 auth.fhd001.com
192.168.16.10 aiapi.fhd001.com
192.168.16.10 pltest.fhd001.com
192.168.16.10 commonapi.fhd001.com
'''
HostsUtils.setHostsData(data209)
import requests
import pytest
import json
import random
import socket

token = "~UAJXAg1dW1YDSoir6oCYtoSM0U1VTlQFVA9cAA5SBwpKAFMG~1~"


# 获取远程IP地址
def test_get_remote_machine_info():
    remote_host = 'wxapi.fhd001.com'
    try:
        print("IP address: {}".format(socket.gethostbyname(remote_host)))
    except socket.error:
        print("{}: {}".format(remote_host, socket.error))


# 用户信息
def test_user():
    url = "https://wxapi.fhd001.com/msaacc/user/getUserInfo.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"token={token}&referer=plwxapi"
    user = requests.post(url=url, data=data, headers=headers)
    # print(user.text)
    a = json.loads(user.text)
    assert 0 == a["scode"]


#   新建寄件地址
def test_New_mail():
    number = random.randint(1, 100)
    url = "https://wxapi.fhd001.com/msaacc/account/saveShippingAddressV2.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "id=0&shippingName=%E5%AF%84%E4%BB%B6%E4%BA%BA%E8%93%9D%EF%BD%9E&shippingMobile=16666666666&" \
           "shippingPhone=&idAuthStatus=NO&isDefault=CLOSE&shippingProvince=%E6%B1%9F%E8%8B%8F%E7%9C%81" \
           "&shippingCity=%E5%8D%97%E4%BA%AC%E5%B8%82&shippingArea=%E9%9B%A8%E8%8A%B1%E5%8F%B0%E5%8C%BA" \
           f"&shippingAddress=%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99%E5%8F%B0+{number}" \
           "&companyName=&idcardInfo=&shippingTown=&shippingZip=" \
           f"&token={token}&referer=plwxapi"
    mail = requests.post(url=url, headers=headers, data=data)
    # print(mail.text)
    a = json.loads(mail.text)
    assert 0 == a["scode"]


#   新建收件地址
def test_Receiving():
    url = "https://commonapi.fhd001.com/fhd/userCustomer/saveUserCustomer.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "customerId=0&name=%E6%94%B6%E4%BB%B6%E4%BA%BA%E9%99%88%EF%BD%9E&cellphone=18888888888" \
           "&province=%E6%B5%99%E6%B1%9F%E7%9C%81&city=%E6%9D%AD%E5%B7%9E%E5%B8%82&area=%E6%BB%A8%E6%B1%9F%E5%8C%BA" \
           "&address=%E6%B1%9F%E9%99%B5%E8%B7%AF%E8%81%9A%E5%85%89&needCount=false&source=0" \
           f"&token={token}&referer=plwxapi"
    Receiving = requests.post(url=url, headers=headers, data=data)
    # print(Receiving.text)
    a = json.loads(Receiving.text)
    assert 0 == a["scode"]


#  下单

def test_placeorder():
    global packageId
    url = "https://wxapi.fhd001.com/msapl/print/savePackageToDelivery.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "changeWlb=1&shareUserId=&barCode=&consigneeList=%5B%7B%22consigneeName%22%3A%22%E6%94%B6%E4%BB%B6%E4%BA%BA%E9%99%88%EF%BD%9E%22%2C%22consigneeMobile%22%3A%2218888888888%22%2C%22consigneePhone%22%3A%22%22%2C%22consigneeProvince%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%22%2C%22consigneeCity%22%3A%22%E6%9D%AD%E5%B7%9E%E5%B8%82%22%2C%22consigneeArea%22%3A%22%E6%BB%A8%E6%B1%9F%E5%8C%BA%22%2C%22consigneeTown%22%3A%22%22%2C%22consigneeAddress%22%3A%22%E6%B1%9F%E9%99%B5%E8%B7%AF%E8%81%9A%E5%85%89%22%2C%22consigneeZip%22%3A%22%22%2C%22consigneeId%22%3A550%7D%5D" \
           "&templateId=&shippingName=%E5%AF%84%E4%BB%B6%E4%BA%BA%E8%93%9D&shippingMobile=16666666666&shippingPhone=" \
           "&companyName=&shippingProvince=%E6%B1%9F%E8%8B%8F%E7%9C%81&shippingCity=%E5%8D%97%E4%BA%AC%E5%B8%82" \
           "&shippingArea=%E9%9B%A8%E8%8A%B1%E5%8F%B0%E5%8C%BA&shippingAddress=%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99%E5%8F%B0" \
           "&shippingCompany=&id=60430&isDefault=OPEN&idAuthStatus=NO&initials=J&nameInitials=JJRL&shippingZip=" \
           "&shippingShopName=&updateTime=1669884811&packageNote=&packageCategory=%E6%9C%8D%E9%A5%B0&packagePostfee=12" \
           "&packageValume=&packageWeight=1&packageId=&packageFlag=&createUser=%7B%22userId%22%3A2799837%2C%22encryptUserId%22%3Anull%2C%22userNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22dbNo%22%3A1%2C%22avatar%22%3A%22https%3A%2F%2Foss.fhd001.com%2Foffline%2Ffhdowx%2FavatarIamge%2F2428ff6568224489a3fa961c7d357a4f.jpg%22%2C%22phoneNumber%22%3Anull%2C%22deliverStatus%22%3Anull%2C%22netpointId%22%3A0%2C%22cpCode%22%3Anull%2C%22netpointCode%22%3Anull%2C%22netpointName%22%3Anull%2C%22extensionCode%22%3Anull%2C%22expert%22%3Anull%2C%22member%22%3Anull%2C%22group%22%3Anull%2C%22idAuthStatus%22%3A%22NO%22%2C%22appId%22%3Anull%2C%22shareFromNeedAuth%22%3Anull%2C%22userRole%22%3A%22PERSONAL%22%2C%22groupAdminUserKey%22%3Anull%2C%22subUserNick%22%3Anull%2C%22timestamp%22%3A1669362333%2C%22fhdCode%22%3A%22111ln%22%2C%22userType%22%3Anull%2C%22first%22%3Afalse%2C%22corpId%22%3Anull%2C%22ip%22%3Anull%2C%22groupId%22%3A0%2C%22groupAdmin%22%3Afalse%2C%22teamRole%22%3Afalse%2C%22groupAdminUserId%22%3A0%2C%22uc%22%3A%22a50fbWliY2NtaGo%3D%22%2C%22deliver%22%3Afalse%2C%22seedExpert%22%3Afalse%2C%22targetUserId%22%3A2799837%2C%22targetUserNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22targetUserDbNo%22%3A1%2C%22pddOrderDbNo%22%3A1%2C%22youzanOrderDbNo%22%3A1%7D" \
           "&userId=2799837&createUserId=2799837&userNick=%E9%99%88%E5%A8%81%E5%BB%B7&title=%E6%9C%8D%E9%A5%B0" \
           "&param=%7B%22expressType%22%3A1%2C%22timeType%22%3A1%2C%22version%22%3A1%2C%22noLossWorry%22%3Atrue%2C%22newExpress%22%3Atrue%2C%22riskArea%22%3Afalse%2C%22totalOriginPrice%22%3A12%2C%22receiveTime%22%3A%222022-12-02%2022%3A00%22%7D&cpCode=JD&source=fhdq&expressType=undefined&tradeMemo=%E4%B8%8B%E5%8D%956666&sendStartTime=1669885404&sendEndTime=1669889004" \
           f"&token={token}&referer=plwxapi"
    placeorder = requests.post(url=url, headers=headers, data=data)
    print(placeorder.text)
    a = json.loads(placeorder.text)
    assert 0 == a["scode"]
    packageId = eval(placeorder.json()['data'])['packageId']
    print(packageId)


# 取消订单
def test_cancel():
    url = "https://wxapi.fhd001.com/msapl/print/cancelPackageToDelivery.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"packageId={packageId}&cpCode=JD&cancelReason=%E6%97%A0%E6%B3%95%E9%80%81%E8%BE%BE%E7%9B%AE%E7%9A%84%E5%9C%B0" \
           f"&token={token}&referer=plwxapi"
    cancel = requests.post(url=url, headers=headers, data=data)
    print(cancel.text)
    a = json.loads(cancel.text)
    assert 0 == a["scode"]


# 重新下单
def test_modify():
    url = "https://wxapi.fhd001.com/msapl/print/savePackageToDelivery.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "changeWlb=1&shareUserId=&barCode=&consigneeList=%5B%7B%22consigneeName%22%3A%22%E6%94%B6%E4%BB%B6%E4%BA%BA%E9%99%88%EF%BD%9E%22%2C%22consigneeMobile%22%3A%2218888888888%22%2C%22consigneePhone%22%3A%22%22%2C%22consigneeProvince%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%22%2C%22consigneeCity%22%3A%22%E6%9D%AD%E5%B7%9E%E5%B8%82%22%2C%22consigneeArea%22%3A%22%E6%BB%A8%E6%B1%9F%E5%8C%BA%22%2C%22consigneeTown%22%3A%22%22%2C%22consigneeAddress%22%3A%22%E6%B1%9F%E9%99%B5%E8%B7%AF%E8%81%9A%E5%85%89%22%2C%22consigneeZip%22%3A%22%22%2C%22consigneeId%22%3A550%7D%5D" \
           "&templateId=&shippingName=%E5%AF%84%E4%BB%B6%E4%BA%BA%E8%93%9D&shippingMobile=16666666666&shippingPhone=" \
           "&companyName=&shippingProvince=%E6%B1%9F%E8%8B%8F%E7%9C%81&shippingCity=%E5%8D%97%E4%BA%AC%E5%B8%82" \
           "&shippingArea=%E9%9B%A8%E8%8A%B1%E5%8F%B0%E5%8C%BA&shippingAddress=%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99%E5%8F%B0" \
           "&shippingCompany=&id=60430&isDefault=OPEN&idAuthStatus=NO&initials=J&nameInitials=JJRL&shippingZip=" \
           "&shippingShopName=&updateTime=1669884811&packageNote=&packageCategory=%E6%9C%8D%E9%A5%B0&packagePostfee=12" \
           "&packageValume=&packageWeight=1&packageId=&packageFlag=&createUser=%7B%22userId%22%3A2799837%2C%22encryptUserId%22%3Anull%2C%22userNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22dbNo%22%3A1%2C%22avatar%22%3A%22https%3A%2F%2Foss.fhd001.com%2Foffline%2Ffhdowx%2FavatarIamge%2F2428ff6568224489a3fa961c7d357a4f.jpg%22%2C%22phoneNumber%22%3Anull%2C%22deliverStatus%22%3Anull%2C%22netpointId%22%3A0%2C%22cpCode%22%3Anull%2C%22netpointCode%22%3Anull%2C%22netpointName%22%3Anull%2C%22extensionCode%22%3Anull%2C%22expert%22%3Anull%2C%22member%22%3Anull%2C%22group%22%3Anull%2C%22idAuthStatus%22%3A%22NO%22%2C%22appId%22%3Anull%2C%22shareFromNeedAuth%22%3Anull%2C%22userRole%22%3A%22PERSONAL%22%2C%22groupAdminUserKey%22%3Anull%2C%22subUserNick%22%3Anull%2C%22timestamp%22%3A1669362333%2C%22fhdCode%22%3A%22111ln%22%2C%22userType%22%3Anull%2C%22first%22%3Afalse%2C%22corpId%22%3Anull%2C%22ip%22%3Anull%2C%22groupId%22%3A0%2C%22groupAdmin%22%3Afalse%2C%22teamRole%22%3Afalse%2C%22groupAdminUserId%22%3A0%2C%22uc%22%3A%22a50fbWliY2NtaGo%3D%22%2C%22deliver%22%3Afalse%2C%22seedExpert%22%3Afalse%2C%22targetUserId%22%3A2799837%2C%22targetUserNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22targetUserDbNo%22%3A1%2C%22pddOrderDbNo%22%3A1%2C%22youzanOrderDbNo%22%3A1%7D" \
           "&userId=2799837&createUserId=2799837&userNick=%E9%99%88%E5%A8%81%E5%BB%B7&title=%E6%9C%8D%E9%A5%B0" \
           "&param=%7B%22expressType%22%3A1%2C%22timeType%22%3A1%2C%22version%22%3A1%2C%22noLossWorry%22%3Atrue%2C%22newExpress%22%3Atrue%2C%22riskArea%22%3Afalse%2C%22totalOriginPrice%22%3A12%2C%22receiveTime%22%3A%222022-12-02%2022%3A00%22%7D&cpCode=JD" \
           "&source=fhdq&expressType=undefined&tradeMemo=%E4%B8%8B%E5%8D%956666&sendStartTime=1669885404" \
           "&sendEndTime=1669889004" \
           f"&token={token}&referer=plwxapi"
    modify = requests.post(url=url, headers=headers, data=data)
    # print(modify.text)
    a = json.loads(modify.text)
    assert 0 == a["scode"]


# 绑定下单伙伴
def test_UserShare():
    url = "https://wxapi.fhd001.com/msaacc/user/scanUserShare.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "shareUserId=2799115" \
           f"&token={token}" \
           "&referer=plwxapi"
    UserShare = requests.post(url=url, headers=headers, data=data)
    # print(UserShare.text)
    a = json.loads(UserShare.text)
    assert 0 == a["scode"]


# 提交订单给下单伙伴
def test_FromPersonal():
    url = "https://wxapi.fhd001.com/msaprint/print/savePackageFromPersonal.do"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "changeWlb=1&shareUserId=2799115&barCode=&consigneeList=%5B%7B%22consigneeName%22%3A%22%E6%94%B6%E4%BB%B6%E4%BA%BA%E9%99%88%EF%BD%9E%22%2C%22consigneeMobile%22%3A%2218888888888%22%2C%22consigneePhone%22%3A%22%22%2C%22consigneeProvince%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%22%2C%22consigneeCity%22%3A%22%E6%9D%AD%E5%B7%9E%E5%B8%82%22%2C%22consigneeArea%22%3A%22%E6%BB%A8%E6%B1%9F%E5%8C%BA%22%2C%22consigneeTown%22%3A%22%22%2C%22consigneeAddress%22%3A%22%E6%B1%9F%E9%99%B5%E8%B7%AF%E8%81%9A%E5%85%89%22%2C%22consigneeZip%22%3A%22%22%2C%22consigneeId%22%3A550%7D%5D" \
           "&templateId=&shippingName=%E5%AF%84%E4%BB%B6%E4%BA%BA%E8%93%9D&shippingMobile=16666666666&shippingPhone=" \
           "&companyName=&shippingProvince=%E6%B1%9F%E8%8B%8F%E7%9C%81&shippingCity=%E5%8D%97%E4%BA%AC%E5%B8%82" \
           "&shippingArea=%E9%9B%A8%E8%8A%B1%E5%8F%B0%E5%8C%BA&shippingAddress=%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99%E5%8F%B0" \
           "&shippingCompany=&id=60430&isDefault=OPEN&idAuthStatus=NO&initials=J&nameInitials=JJRL&shippingZip=" \
           "&shippingShopName=&updateTime=1669884811&packageNote=%E7%BB%91%E5%AE%9A%E4%BC%99%E4%BC%B4%E4%B8%8B%E5%8D%95%E6%A3%95%E8%89%B2%E8%8A%B1%E8%89%B2" \
           "&packageCategory=%E6%9C%8D%E9%A5%B0&packagePostfee=0&packageValume=&packageWeight=1&packageId=&packageFlag=&createUser=%7B%22userId%22%3A2799837%2C%22encryptUserId%22%3Anull%2C%22userNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22dbNo%22%3A1%2C%22avatar%22%3A%22https%3A%2F%2Foss.fhd001.com%2Foffline%2Ffhdowx%2FavatarIamge%2F2428ff6568224489a3fa961c7d357a4f.jpg%22%2C%22phoneNumber%22%3Anull%2C%22deliverStatus%22%3Anull%2C%22netpointId%22%3A0%2C%22cpCode%22%3Anull%2C%22netpointCode%22%3Anull%2C%22netpointName%22%3Anull%2C%22extensionCode%22%3Anull%2C%22expert%22%3Anull%2C%22member%22%3Anull%2C%22group%22%3Anull%2C%22idAuthStatus%22%3A%22NO%22%2C%22appId%22%3Anull%2C%22shareFromNeedAuth%22%3Anull%2C%22userRole%22%3A%22PERSONAL%22%2C%22groupAdminUserKey%22%3Anull%2C%22subUserNick%22%3Anull%2C%22timestamp%22%3A1669362333%2C%22fhdCode%22%3A%22111ln%22%2C%22userType%22%3Anull%2C%22first%22%3Afalse%2C%22corpId%22%3Anull%2C%22ip%22%3Anull%2C%22groupId%22%3A0%2C%22groupAdmin%22%3Afalse%2C%22teamRole%22%3Afalse%2C%22groupAdminUserId%22%3A0%2C%22uc%22%3A%22ab96bWliY2NtaGg%3D%22%2C%22deliver%22%3Afalse%2C%22seedExpert%22%3Afalse%2C%22targetUserId%22%3A2799837%2C%22targetUserNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22targetUserDbNo%22%3A1%2C%22pddOrderDbNo%22%3A1%2C%22youzanOrderDbNo%22%3A1%7D" \
           "&userId=2799837&createUserId=2799837&userNick=%E9%99%88%E5%A8%81%E5%BB%B7&title=%E6%9C%8D%E9%A5%B0" \
           f"&token={token}&referer=plwxapi"
    FromPersonal = requests.post(url=url, headers=headers, data=data)
    # print(FromPersonal.text)
    a = json.loads(FromPersonal.text)
    assert 0 == a["scode"]


# 寄大件
def test_large():
    url = "https://wxapi.fhd001.com/msapl/print/savePackageToDelivery.do "
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = "changeWlb=1&consigneeList=%5B%7B%22consigneeName%22%3A%22%E6%94%B6%E4%BB%B6%E4%BA%BA%E9%99%88%EF%BD%9E%22%2C%22consigneeMobile%22%3A%2218888888888%22%2C%22consigneePhone%22%3A%22%22%2C%22consigneeProvince%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%22%2C%22consigneeCity%22%3A%22%E6%9D%AD%E5%B7%9E%E5%B8%82%22%2C%22consigneeArea%22%3A%22%E6%BB%A8%E6%B1%9F%E5%8C%BA%22%2C%22consigneeTown%22%3A%22%22%2C%22consigneeAddress%22%3A%22%E6%B1%9F%E9%99%B5%E8%B7%AF%E8%81%9A%E5%85%89%22%2C%22consigneeZip%22%3A%22%22%2C%22consigneeId%22%3A551%7D%5D" \
           "&param=%7B%22expressType%22%3A%22JZKH%22%2C%22version%22%3A1%2C%22newExpress%22%3Atrue%2C%22noLossWorry%22%3Atrue%2C%22payType%22%3A1%2C%22deliveryType%22%3A3%2C%22totalOriginPrice%22%3A65%7D&shippingName=%E5%AF%84%E4%BB%B6%E4%BA%BA%E8%93%9D&shippingMobile=16666666666" \
           "&shippingPhone=&companyName=&shippingProvince=%E6%B1%9F%E8%8B%8F%E7%9C%81&shippingCity=%E5%8D%97%E4%BA%AC%E5%B8%82&shippingArea=%E9%9B%A8%E8%8A%B1%E5%8F%B0%E5%8C%BA&shippingAddress=%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99%E5%8F%B0&shippingCompany=&id=60431&isDefault=OPEN" \
           "&idAuthStatus=NO&initials=J&nameInitials=JJRL&shippingZip=&shippingShopName=&updateTime=1669885861&packageNote=" \
           "&packageCategory=%E6%9C%8D%E9%A5%B0&packagePostfee=58.5&packageValume=&packageWeight=61&packageId=&packageFlag=" \
           "&createUser=%7B%22userId%22%3A2799837%2C%22encryptUserId%22%3Anull%2C%22userNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22dbNo%22%3A1%2C%22avatar%22%3A%22https%3A%2F%2Foss.fhd001.com%2Foffline%2Ffhdowx%2FavatarIamge%2F2428ff6568224489a3fa961c7d357a4f.jpg%22%2C%22phoneNumber%22%3Anull%2C%22deliverStatus%22%3Anull%2C%22netpointId%22%3A0%2C%22cpCode%22%3Anull%2C%22netpointCode%22%3Anull%2C%22netpointName%22%3Anull%2C%22extensionCode%22%3Anull%2C%22expert%22%3Anull%2C%22member%22%3Anull%2C%22group%22%3Anull%2C%22idAuthStatus%22%3A%22NO%22%2C%22appId%22%3Anull%2C%22shareFromNeedAuth%22%3Anull%2C%22userRole%22%3A%22PERSONAL%22%2C%22groupAdminUserKey%22%3Anull%2C%22subUserNick%22%3Anull%2C%22timestamp%22%3A1669362333%2C%22fhdCode%22%3A%22111ln%22%2C%22userType%22%3Anull%2C%22first%22%3Afalse%2C%22corpId%22%3Anull%2C%22ip%22%3Anull%2C%22groupId%22%3A0%2C%22groupAdmin%22%3Afalse%2C%22teamRole%22%3Afalse%2C%22groupAdminUserId%22%3A0%2C%22uc%22%3A%22a6f7bWliY2NtaGI%3D%22%2C%22deliver%22%3Afalse%2C%22seedExpert%22%3Afalse%2C%22targetUserId%22%3A2799837%2C%22targetUserNick%22%3A%22%E9%99%88%E5%A8%81%E5%BB%B7%22%2C%22targetUserDbNo%22%3A1%2C%22pddOrderDbNo%22%3A1%2C%22youzanOrderDbNo%22%3A1%7D" \
           "&userId=2799837&createUserId=2799837&userNick=%E9%99%88%E5%A8%81%E5%BB%B7&cpCode=DBKD&expressType=JZKH" \
           "&tradeMemo=%E5%AF%84%E5%A4%A7%E4%BB%B6&sendStartTime=1669942800&sendEndTime=1669950000" \
           f"&token={token}&referer=plwxapi"
    large = requests.post(url=url, headers=headers, data=data)
    print(large.text)
    a = json.loads(large.text)
    assert 0 == a["scode"]
