##
number = '79001231231'
password = 'qwerty'
##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
##
path = r"C:\Users\Артём Владимирович\Downloads\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get('https://yandex.ru')
search = driver.find_element_by_id('text')
search.send_keys('фото бараша')
search.send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text('Картинки').click()

tabs = driver.window_handles  # список
driver.switch_to.window(tabs[1])
img1 = driver.find_elements_by_class_name('serp-item__link')  # список элементов
img_link = img1[1].get_attribute('href')
driver.get(img_link)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Открыть')))
# driver.find_element_by_partial_link_text('Открыть').click() #не работает
element.click()
tabs1 = driver.window_handles
driver.switch_to.window(tabs1[2])

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# получили бараша

driver.get('https://vk.com/id507121631')
driver.find_element_by_id('quick_email').send_keys(number)
driver.find_element_by_id('quick_pass').send_keys(password)
driver.find_element_by_id('quick_login_button').click()

wait = WebDriverWait(driver, 5)

elem = wait.until(EC.visibility_of_element_located((By.ID, 'post_field')))
elem.clear()
elem.send_keys('Если бараш наберет 5 лайков, я выложу Нюшу\n\
p.s. Этот пост был опубликован с помощью Python')
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="send_post"]').click()
#driver.close()