from suds.client import Client
from suds.sudsobject import asdict
import json


# url = 'http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl'
# client = Client(url)
# print(client)
# print(dir(client.items))
# print(client.messages)
# print(client.service)
# print(dir(client.service))
# print(client.service.qqCheckOnline(qqCode=389951389))
# print(client.service.qqCheckOnline())


# print(dir(client))


url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?WSDL'
client = Client(url)
# print(client)

# print(client.service.getDatabaseInfo())
print(client.service.getMobileCodeInfo(mobileCode=18025847742))
print(client.service.getMobileCodeInfo(17376747374))
print(client.service.getMobileCodeInfo())
# print(client.service.getMobileCodeInfo())
