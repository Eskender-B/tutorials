from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://resumes.indeed.com/search?q=anytitle%3A(business%20analyst)")
sign_in_link = driver.find_element_by_xpath('/html/body/div[1]/div[1]/nav/div/div/div[2]/a')

sign_in_link.click()
email = driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div/section/form/div[1]/div[1]/div/div[2]/input')
email.clear()
email.send_keys('')

passwd = driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div/section/form/div[1]/div[2]/div/div/div[2]/input')
passwd.clear()
passwd.send_keys()_

time.sleep(120)
#button = driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div/section/form/button')
button = driver.find_element_by_xpath('//*[@id="login-submit-button"]')
button.click()


#page_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/div/div/div[4]/div/nav/ul[1]')
page_list = driver.find_element_by_xpath('//*[@id="search-results"]/div[4]/div/nav/ul[1]')
max_page_num = int(page_list.find_elements_by_tag_name('li')[-1].text)

#next_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/div/div/div[4]/div/nav/ul[2]/li[2]/button')
next_btn = driver.find_element_by_xpath('//*[@id="search-results"]/div[4]/div/nav/ul[2]/li[2]/button')


for i in range(max_page_num):
    print(f'Downloading resumes from page {i+1}')
    #unordered_list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[2]/div[1]/div/div/div[3]/ul')
    unordered_list = driver.find_element_by_xpath('//*[@id="result-list"]')
    items = unordered_list.find_elements_by_css_selector('a[data-cauto-id=resume_card_name')
    for item in items:
        item.click()
        dwnld_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="resume-preview"]/div[1]/div/div/div/div[2]/button[3]'))
    )
        dwnld_button.click()
    if i != (max_page_num -1):
        next_btn.click()
        time.sleep(10)
driver.close()
