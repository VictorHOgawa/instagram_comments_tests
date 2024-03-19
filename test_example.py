# test_example.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

i = 0

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/marciaconradolorena/")

# close_prompt = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.CLASS_NAME,"_a9zr"))
# close_prompt.click()
time.sleep(20)

latest_post = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.CLASS_NAME,"_aabd"))
latest_post.click()


# comment_ids = []

# load_more_path = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/li/div"


# # "Load more comments" until 2 clicks
# while i < 3:
#     try:
#         WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, load_more_path))).click()
#         time.sleep(1.42)
                
#     except:
#         print("No more 'LOAD MORE COMMENTS' button to be clicked")
#         break
    
# # "View Replies" if there's any
# view_reply_path = 'li > ul > li > div > button[class="_acan _acao _acas _aj1-"]'

# WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, view_reply_path)))
# view_reply_buttons = driver.find_elements(By.CSS_SELECTOR, view_reply_path)

# for button in range(len(view_reply_buttons)):
#     view_reply_buttons[button].click()
#     time.sleep(1.32)

# time.sleep(5.8)
# comment = driver.find_elements(By.CLASS_NAME, "_a9zj")

# for c in comment:
#     container = c.find_element(By.CLASS_NAME,'_a9zr')

#     WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/a')))
#     commentid = c.find_element(By.XPATH, '//div[2]/div/a').get_attribute("href")
  
#     comment_ids.append(commentid)

#     print(commentid)