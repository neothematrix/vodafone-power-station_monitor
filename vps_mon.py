import json
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import \
    presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
webdriver = webdriver.Chrome(
    options=chrome_options
)

if (len(sys.argv) >= 3):
    vps_ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

url = 'http://%s/' % vps_ip

with webdriver as driver:
    wait = WebDriverWait(driver, 3)

    driver.get(url)

    # login
    username = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input").send_keys(username)
    password = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/input").send_keys(password)
    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input")
    driver.execute_script("arguments[0].click();", login_button)

    wait.until(presence_of_element_located((By.ID, "look_4")))

    # save CSRF token to reuse
    csrf_token = re.search(
        "csrf_token = '([A-Z0-9]+)'", driver.page_source).group(1)

    # open SFP status json XHR page
    sfp_status_page_url = url+'data/statussupportsfpstatus.json?_=' + \
        str(int(time.time()))+'&csrf_token='+csrf_token
    driver.get(sfp_status_page_url)
    sfp_status_json = json.loads(
        re.search("<body>(.*)<\/body>", driver.page_source).group(1))

    # open status json XHR page
    status_page_url = url+'data/statussupportstatus.json?_=' + \
        str(int(time.time()))+'&csrf_token='+csrf_token
    driver.get(status_page_url)
    status_json = json.loads(
        re.search("<body>(.*)<\/body>", driver.page_source).group(1))

    # merge and transform the lists into a better manageable dict
    status_json_dict = {}
    for item in sfp_status_json+status_json:
        status_json_dict.update(item)
    print(json.dumps(status_json_dict))

    driver.close()
