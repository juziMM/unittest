from Crm_page.base import base
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium import webdriver

class Login(base):
    #找到输入账号的位置
    def search_un(self):
        return self.find(By.NAME,"userNum")
    #找到输入密码的位置
    def search_pw(self):
        return self.find(By.NAME,"userPw")
    #找到点击登录位置
    def search_lg(self):
        return self.find(By.ID,"in1")

    #编写测试用例
    def search_test(self,un,pw):
        time.sleep(5)
        #输入账号
        self.search_un().send_keys(un)
        time.sleep(2)
        #输入密码
        self.search_pw().send_keys(pw)
        time.sleep(2)
        #点击登录
        self.search_lg().click()




