import requests
from selenium import webdriver
import time


class GetTeamBitionEvents(object):

    def __init__(self):
        self.company_url = 'https://www.teambition.com/organization/'
        # 登录Teambition后默认进入的企业的首页，url中有企业的id,企业一旦创建，id就不会改变
        self.company_id = '5c3d900b12532300010f26c4'
        # 在开发者中心OAuth2配置处填的回调地址，与这里拼接的回调地址保持一致
        self.callback_url = self.company_url + self.company_id
        # 在企业后台管理中的应用管理处进入teambition开发者中心，创建应用时的Client ID
        self.client_id = 'd02c31d0-624a-11e9-a061-1d71fe55a756'
        # 在企业后台管理中的应用管理处进入teambition开发者中心，创建应用时的Client Secret
        self.client_secret = '441ff8d8-982e-4926-8d30-80b6fa819c61'
        self.auth_url = 'https://account.teambition.com/oauth2/authorize?client_id=' + self.client_id + \
                        '&redirect_uri=' + self.callback_url
        self.user_email = 'wangb@botsoft.cn'
        self.user_password = 'Wb879128630'
        self.token_url = 'https://account.teambition.com/oauth2/access_token'

    def get_code(self):
        """
        模拟浏览器获取code
        """
        # 声明一个浏览器对象，指定使用chrome浏览器
        browser = webdriver.Chrome()
        try:
            # get打开指定的url，传入要打开的url
            browser.get(self.auth_url)
            # 通过find_element_by_name获取到网页标签，send_keys()输入内容
            browser.find_element_by_name('email').send_keys(self.user_email)
            browser.find_element_by_name('password').send_keys(self.user_password)
            # 通过find_element_by_class_name获取到网页标签，click()点击
            # 注意class名中的空格是表示父子级的关系，如果有空格，则class_name只去最后一段，然后还要避免有同名的class，为了
            # 避免取错标签，优先根据id或name等其他方式取
            browser.find_element_by_class_name('anim-blue-all').click()

            time.sleep(2)
            # browser.find_element_by_name('allow').click()
            browser.find_element_by_class_name('authorize-btn').click()
            code = browser.current_url.split('=')[1]
            print(browser.current_url.split('=')[1])
            time.sleep(10)
            browser.close()
            return code
        except Exception as e:
            print("模拟登录获取code失败：{}".format(e))
            browser.close()

    def get_token(self):
        """
        根据code获取token
        """
        code = self.get_code()
        access_data = {'client_id': self.client_id, 'client_secret': self.client_secret, 'code': code}
        result = requests.post(self.token_url, data=access_data)
        # print(result)
        print(result.text)
        return result.text


if __name__ == '__main__':
    tb = GetTeamBitionEvents()
    token = tb.get_token()
    print(token)
