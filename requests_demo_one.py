# coding=utf-8
# import requests
#
#
# response = requests.get("https://www.baidu.com")
# # response.encoding('gbk')
# # print(response.text)
# print(response.content.decode('utf-8'))


# coding=utf-8
# import requests
#
#
# url = "https://s.taobao.com/search?"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     "Referer": "https://www.taobao.com/",
#     "Upgrade-Insecure-Requests": '1',
# }
# key_dict = {"wd": "python"}
# response = requests.get(url, params=key_dict, headers=headers)
# print(response.text)


# coding=utf-8
# import requests
#
#
# url = "https://www.sogou.com/tx?"
# key_dict = {"query": "python"}
# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",}
# response = requests.get(url, params=key_dict, headers=headers)
# print(response.text)


# coding=utf-8
# import urllib2
# import urllib
# import time
# import json
#
#
# url = "https://fanyi.qq.com/api/translate"
# headers = {
#     "Origin": "https://fanyi.qq.com",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     # "Cookie": "pgv_pvid=8934651044; pgv_pvi=4193566720; RK=BE5x9QjBaP; ptcz=ed332025191b05fbcb10c0a65925be52d81f88e60c566ab43ab2da73421a7128; tvfe_boss_uuid=774827fb6af54e3f; o_cookie=879128630; pac_uid=1_879128630; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b444b7ce7c3-0878aea7f766f3-37c153e-1327104-16b444b7ce867d%22%2C%22%24device_id%22%3A%2216b444b7ce7c3-0878aea7f766f3-37c153e-1327104-16b444b7ce867d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; fy_guid=60d205f6-fdd5-467a-a0a3-d8be9014b657; ADHOC_MEMBERSHIP_CLIENT_ID1.0=89992c70-4530-3528-ceb1-f0de748ab7f6; gr_user_id=9b034d2c-f92b-4b8b-a349-d9e330396247; grwng_uid=2aa153f5-bd77-49c3-a668-cb47eda16c8a; ptui_loginuin=389951389; qq_openid=D1CC22212A3EDA6838633619511BB3D9; qq_access_token=76A4D6F161E79392287304FA5CF0A6C8; qq_client_id=101487368; ts_uid=1716188860; ts_refer=www.baidu.com/link; pgv_si=s8044222464; 8507d3409e6fad23_gr_session_id=5aac5f38-2d05-4068-87bf-56770587208c; 8c66aca9f0d1ff2e_gr_session_id=5f271c76-175a-4045-a3fc-4ff2aa869b1e; qtv=30c0e3d923987a75; qtk=41OK/4ufKOTXn6p4y/zVCyWeVchU1G/GsRrGid1WsSCiZE/ag2CWiGPQGAeh1mHToj2femMo8Fwy5LKe2GWqgE9yg9GIMUVUK2JTch+Lm6Ootam28Jd8iSDTbECdeDhJb4hX9QwmXArSV4cZTnCPqg==; openCount=4; 8507d3409e6fad23_gr_session_id_5aac5f38-2d05-4068-87bf-56770587208c=true",
#     # "Referer": "https://fanyi.qq.com",
#     # "Host": "fanyi.qq.com",
#     # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     # "Accept": "application/json, text/javascript, */*; q=0.01"
# }
# time_str = str(int(1000 * time.time()))
# key_dict = {
#     "source": "zh",
#     "target": "en",
#     "sourceText": "发送 POST 请求",
#     "sessionUuid ": "translate_uuid" + time_str
#     }
# data = urllib.urlencode(key_dict)
# request = urllib2.Request(url, data=data, headers=headers)
# response = urllib2.urlopen(request)
# print(response.code)
# html = response.read()
# result = json.loads(html)
# print(result['translate']['records'][0]['targetText'])


# coding=utf-8
import requests
import time
import json


url = "https://fanyi.qq.com/api/translate"
headers = {
    "Origin": "https://fanyi.qq.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
time_str = str(int(1000 * time.time()))
key_dict = {
    "source": "zh",
    "target": "en",
    "sourceText": "发送 POST 请求",
    "sessionUuid ": "translate_uuid" + time_str
    }
response = requests.post(url, data=key_dict, headers=headers)
print(response.status_code)
# result = json.loads(response.text)
result = response.json()
# print('result', result)
print(result['translate']['records'][0]['targetText'])
