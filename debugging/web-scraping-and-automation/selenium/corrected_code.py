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
username_text_box.send_keys('your_username')  # Replace 'your_username' with your actual GitHub username
password_text_box = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password_text_box.clear()
password_text_box.send_keys('your_password')  # Replace 'your_password' with your actual GitHub password
password_text_box.send_keys(Keys.ENTER)

new_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-hydro-click and contains(@href, '/new')]")))
new_button.click()

repo_name_text_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="repository-name-input"]')))
repo_name_text_box.send_keys('idk1')
time.sleep(2)
repo_name_text_box.send_keys(Keys.ENTER)

upload_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-ga-click][data-hydro-click][href$='/upload']")))
upload_link.click()

file_input = driver.find_element_by_css_selector('input[type="file"]')
upload_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'research-question.txt')
file_input.send_keys(upload_file_path)

time.sleep(10)

commit_changes_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-file')))
commit_changes_button.click()

time.sleep(1)

uploaded_file = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'research-question.txt')))
uploaded_file.click()

text_element = wait.until(EC.presence_of_element_located((By.ID, 'raw-url')))
text_element.click()
time.sleep(2)

select_text = driver.find_element_by_css_selector('.CodeMirror-lines')
select_text.click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(5)

driver.quit()