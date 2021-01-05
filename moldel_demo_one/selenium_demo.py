from selenium import webdriver
import time


# 声明浏览器
browser = webdriver.Chrome()
try:
    # get打开指定的url，传入要打开的url,以淘宝网为例
    browser.get('https://www.taobao.com/')
    # 通过find_element_by_name获取到网页标签，send_keys()输入内容,在搜索栏输入python
    browser.find_element_by_name('q').send_keys('python')
    time.sleep(1)
    '''
    通过find_element_by_class_name获取到网页标签，click()点击
    注意class名中的空格是表示父子级的关系，如果有空格，则class_name只取最后一段，然后还要避免有同名的class，为了
    避免取错标签，优先根据id或name等其他方式取
    淘宝网的搜索按钮class name为btn-search tb-bg,用btn-search tb-bg取时报错,用tb-bg取则成功
    '''
    # browser.find_element_by_class_name('btn-search tb-bg').click()  # 报错
    browser.find_element_by_class_name('tb-bg').click()  # 成功
    time.sleep(5)
    # 点击"密码登录"按钮
    # browser.find_element_by_class_name('forget-pwd J_Quick2Static').click()  # 报错
    browser.find_element_by_class_name('J_Quick2Static').click()  # 正常
    time.sleep(10)
    browser.close()
except Exception as e:
    print("模拟登录失败：{}".format(e))
    browser.close()
