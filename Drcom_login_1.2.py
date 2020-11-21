#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from subprocess import run

  
def Login():
    # 打开谷歌浏览器
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless') #增加无界面选项
    chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    url = "https://drcom.szu.edu.cn/a70.htm" #登录网址,填校园网登录界面网址
    Name = "name"  #账号，填入自己的
    Password = "******"  #密码，同上
    
    # 访问网址
    driver.get(url)
    driver.implicitly_wait(20)  # 隐性等待，最长等20秒
    # 输入账号
    driver.find_element_by_id("VipDefaultAccount").send_keys(Name)
    # 输入密码
    driver.find_element_by_id("VipDefaultPassword").send_keys(Password)
    # 点击登录按钮
    driver.find_element_by_xpath("//*[@name='f1']/div[@id='btn']/input[@id='login']").click()
    driver.quit()
    
def test_net():
    #检查网络是否联通,利用此函数将不会主动弹出命令行窗口
    res = run('ping 8.8.8.8',shell=True)
    if res.returncode:
        Login()
    else:
        print('ping ok')

if __name__ == "__main__":
    test_net()
    

