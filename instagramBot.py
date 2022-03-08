from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def inputInfo():
	username = input("Kullanici adini gir:")
	password = input("Sifreni gir:")
	spam_profile = input("Mesaj gondericeginiz kisinin kullanici adiniz gir:")
	message = input("Gonderilecek mesaji gir:")
	message_number = input("kac kez goncerilecegini gir:")
	return (username,password,spam_profile,message,message_number)

info = inputInfo()
print(info)
driver_path = "./chromedriver"
browser = webdriver.Chrome(driver_path)
url = "https://www.instagram.com/"
browser.get(url)
time.sleep(3)	

username_entry = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password_entry = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

username_entry.send_keys(info[0])
password_entry.send_keys(info[1])

enter_button = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
enter_button.click()
time.sleep(5)

browser.get(url+info[2])

time.sleep(3)
message_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")
message_button.click()							

time.sleep(3)
not_now = browser.find_element_by_css_selector(".HoLwm")
not_now.click()

time.sleep(3)
message_area = browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")

for i in range(0,int(info[4])):
	message_area.send_keys(info[3])
	send_button = browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
	send_button.click()

browser.close()

