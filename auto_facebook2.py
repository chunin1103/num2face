from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import urllib.request
from sourcefile import sourcedata
import os

#nonrelated: create a folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#setup selenium
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path=r'C:\Python38\Scripts\chromedriver.exe', options=options)

# 2. Mo thu mot trang web
browser.get("https://www.facebook.com/")

# 2a. Login
txt_userID = browser.find_element_by_id("email") #ID
txt_userID.send_keys("iug47775@zwoho.com")

txt_password = browser.find_element_by_name("pass") #password
txt_password.send_keys("Neji1103!!  ")

# 2b Submit form

txt_password.send_keys(Keys.ENTER)
sleep (1.23)

# 3 Get facebook link

# 3a list of links from source
list_link = list(sourcedata.keys())

# 3b loop for each links
m = 0 #first loop

for m in range(1099, 2000):
    # save first link for latter user
    initial_link = list_link[m]
    
    # get first link to start crawling: facebook.com/userID
    browser.get(list_link[m])
    sleep (2.5)

    facebook_link = browser.current_url
    if 'profile' not in facebook_link:
        photo_link = facebook_link + "photos" #facebook/userID/photos

    else:
        photo_link = facebook_link + "&sk=photos" #facebook?userID=12312&sk=photos

    browser.get(photo_link)
    sleep (2)

    #find all images from profile
    # images = browser.find_elements_by_tag_name('img')
    images = browser.find_elements_by_xpath("//div[@id='mount_0_0']//img")

    #find phone number that correlate with the link for latter use
    correlate_number = sourcedata[initial_link]

    print(m)
    n = -1
    #create a save location
    save_location = "E:/Projects/......Num2face/Code/"
    #this function is coded on top
    createFolder(save_location + correlate_number)

    for image in images:
        n += 1
        if n < 18:
            #get all image links
            img_link = image.get_attribute('src')
            #download all files
            urllib.request.urlretrieve(img_link, save_location + correlate_number + "/filename" + str(n) + ".png")
            # print(img_link)    

    sleep(2.52)
    if m == 1300:
        sleep(50.3)
    if m == 1600:
        sleep(50.1)

#initial stop is at #1097





