import os
import time

from .db import DataBaseManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

data_base = DataBaseManager()

URL = str(os.environ.get('URL'))


def proc_main():
    browser_driver = webdriver.Firefox()
    browser_driver.get(URL)
    last_uuid = None
    while True:
        div = browser_driver.find_element_by_xpath("//div[@class='fairness-modal-link']")
        div.click()
        table = browser_driver.find_element_by_xpath("//div[@data-modal-type='crash_history_index']")
        time.sleep(1)
        rows = table.find_elements(By.TAG_NAME, "tr")
        if len(rows) > 1:
            row = rows[1]
            col = row.find_elements(By.TAG_NAME, "td")
            uuid = col[2].text
            rate = col[1].text
            date_hour = col[0].text
            if last_uuid != uuid:
                last_uuid = uuid
                data_base.insert_data_into_crash_canvas_history((uuid, rate, date_hour))
        div = browser_driver.find_element_by_xpath("//div[@class='close']")
        div.click()
