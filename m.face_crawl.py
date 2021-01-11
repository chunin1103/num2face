from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path=r'C:\Python38\Scripts\chromedriver.exe')

# 2. Mo thu mot trang web
browser.get("http://m.facebook.com")

# 2a. Login
txt_userID = browser.find_element_by_id("m_login_email") #ID
txt_userID.send_keys("iug47775@zwoho.com")

txt_password = browser.find_element_by_name("pass") #password
txt_password.send_keys("Neji1103!!  ")

#2b Submit form

txt_password.send_keys(Keys.ENTER)


# 3. Dung chuong trinh 5 giay
sleep (7)
notnow_click = browser.find_element_by_xpath("//*[@id='root']/table/tbody/tr/td/div/div[3]/a")
notnow_click.click()
sleep (7)

# 4. Dong trinh duyet
# browser.close()