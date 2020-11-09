import requests
import sys
import io,time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码

'''无头chrome'''
chrome=r'/usr/local/bin/chromedriver'
# browser = webdriver.Chrome(executable_path=chrome)#弹出浏览器

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path=chrome,chrome_options=chrome_options)
#登录页面
# url = r'https://m.touker.com/account/login/custNoLogin.do'
#     https://m.touker.com/account/login/index.htm?source=stock_trade_h5&referrer=https://m.touker.com/trading/trade/sell#/oauth/custLogin
# url=r'file:///C:/Users/wang/Desktop/%E7%99%BB%E5%BD%95.html#/'
url=r'https://m.touker.com/account/login/index.htm?source=stock_trade_h5&referrer=https://m.touker.com/trading/trade/sell#/oauth/custLogin'
browser.get(url)
# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)
#输入用户名
with open('./config.json', 'r') as f:
    huabao=json.load(f)
usr=huabao['custno']
pwd=huabao['password']
username = browser.find_element_by_class_name('hb-input-core')
username.send_keys(usr)
#输入密码
password = browser.find_element_by_class_name('hide_input')
password.send_keys(pwd)

login_button = browser.find_element_by_css_selector('[class="hb-btn hb-btn-primary hb-btn-normal"]')
login_button.click()

time.sleep(2)
# # 获取cookie列表
cookie_list=browser.get_cookies()
print(cookie_list)

def get_cookie():
    return cookie_list

