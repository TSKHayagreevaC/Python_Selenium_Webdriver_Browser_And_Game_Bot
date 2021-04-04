from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-39349.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Srikanth")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Hayagreeva")

email = driver.find_element_by_name("email")
email.send_keys("sriknth@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()




