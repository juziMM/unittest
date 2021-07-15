from Z_crm_page.Crm_page.base import base
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# class Add(base):
#     # 切换frame
#     # 定位到 iframe 并进行切换
#     def search_frame(self):
#         self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('frame')[1])
#         self.driver.find_element_by_xpath(
#             '/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]').click()
#         self.driver.find_element_by_link_text('添加员工').click()
#         self.driver.switch_to.default_content()  # 返回默认frame
#         self.driver.implicitly_wait(2)
#
#     # 定位到员工添加的位置
#     def search_addYG(self):
#         self.driver.switch_to.frame('mainFrame')
#         self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[2]/input').click()
#
#     # 找到输入姓名的位置
#     def search_name(self):
#         return self.find(By.NAME,"userName")
#
#     # 找到输入年龄的位置
#     def search_age(self):
#         return self.find(By.NAME,"userAge")
#
#
#     # 找到输入账号的位置
#     def search_usernum(self):
#         return self.find(By.NAME,"userNum")
#
#     #找到输入密码的位置
#     def search_userpw(self):
#         return self.find(By.NAME,"userPw")
#
#     #找到输入添加人的位置
#     def search_addman(self):
#         return self.find(By.NAME,"userAddman")
#
#     #找到点击添加的位置
#     def search_addclick(self):
#         return self.find(By.XPATH,"/html/body/form/table[2]/tbody/tr/td[2]/input")
#
#     #编写测试用例
#     def search_test1(self, names, age, usernm, userpw, useraddman):
#         time.sleep(5)
#         # 输入姓名
#         self.search_name().send_keys(names)
#         time.sleep(2)
#         # 输入年龄
#         self.search_age().send_keys(age)
#         time.sleep(2)
#         # 输入账号
#         self.search_usernum().send_keys(usernm)
#         time.sleep(2)
#         # 输入密码
#         self.search_userpw().send_keys(userpw)
#         time.sleep(2)
#         # 输入添加人
#         self.search_addman().send_keys(useraddman)
#         time.sleep(2)
#         # 点击添加
#         self.search_addclick().click()
