from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://github.com/')

wait = WebDriverWait(driver, 15)

sign_in_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'HeaderMenu-link--sign-in')))
sign_in_button.click()

username_text_box = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
username_text_box.clear()
username_text_box.send_keys('username')
password_text_box = driver.find_element_by_id(By.ID, 'password')
# password_text_box = driver.find_element_by_id('password')
password_text_box.clear()
password_text_box.send_keys('password')
password_text_box.send_keys(Keys.ENTER)

new_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-hydro-click and contains(@href, '/new')]")))
new_button.click()

repo_name_text_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="repository-name-input"]')))
repo_name_text_box.send_keys('idk1')
time.sleep(2)
repo_name_text_box.send_keys(Keys.ENTER)

upload_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-ga-click][data-hydro-click][href$='/upload']")))
upload_link.click()

upload_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'research-question.txt')
# file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
file_input.send_keys(upload_file_path)

time.sleep(10)

commit_changes_button = driver.find_element_by_class_name(By.CLASS_NAME, 'js-blob-submit')
# commit_changes_button = driver.find_element_by_class_name('js-blob-submit')
commit_changes_button.click()

time.sleep(1)

uploaded_file = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'research-question.txt')))
uploaded_file.click()

text_element = wait.until(EC.presence_of_element_located((By.ID, 'read-only-cursor-text-area')))
ActionChains(driver).move_to_element(text_element).click().double_click().key_down(Keys.CONTROL).send_keys('c').perform()
# ActionChains(driver).move_to_element(text_element).click().double_click(text_element).key_down(Keys.CONTROL).send_keys('c').perform()

time.sleep(5)

driver.quit()