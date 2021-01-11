from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import urllib.request


# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path=r'C:\Python38\Scripts\chromedriver.exe')

# 2. Mo thu mot trang web
browser.get("http://mbasic.facebook.com")

# 2a. Login
txt_userID = browser.find_element_by_id("m_login_email") #ID
txt_userID.send_keys("iug47775@zwoho.com")

txt_password = browser.find_element_by_name("pass") #password
txt_password.send_keys("Neji1103!!  ")

# 2b Submit form

txt_password.send_keys(Keys.ENTER)


# 3. Dung chuong trinh 5 giay
sleep (2.5)
skipNotnow_click = browser.find_element_by_xpath("//*[@id='root']/table/tbody/tr/td/div/div[3]/a")
skipNotnow_click.click()
sleep (3.4)


# 4. Den trang ca nhan nguoi dung
browser.get("https://mbasic.facebook.com/winthanglevan?id=100002512795022")
sleep (2.4)

# 5. Lay anh
browser.get("https://mbasic.facebook.com/winthanglevan/photos?id=100002512795022")
sleep (1.2)
all_photos = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/section/a")
all_photos.click()
sleep (1.2)

# 5a Download images
images = browser.find_elements_by_tag_name('img')
n = 0
for image in images:
    n += 1
    img_link = image.get_attribute('src')
    # urllib.request.urlretrieve(img_link, "filename" + str(n) + ".png")
    print(img_link + str(n))
# 7. Dong trinh duyet
# 7. Dong trinh duyet
# 7. Dong trinh duyet
# 7. Dong trinh duyet
# 7. Dong trinh duyet
# browser.close()