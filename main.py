from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.in/Whirlpool-1-5T-MAGICOOL-PRO-COPR/dp/B07P5HJJW8/ref=lp_22176183031_1_1")
# price = driver.find_element_by_id("a-autoid-7")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector("documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li/[3]/a')
# print(bug_link)

# event_times = driver.find_element_by_css_selector(".event-widget time")
# print(event_times)

# event_times = driver.find_element_by_css_selector(".event-widget time")
# event_names = driver.find_element_by_css_selector("event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }

# driver.close()
driver.quit()

