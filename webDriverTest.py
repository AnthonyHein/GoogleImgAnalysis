#-------------------------------------------------------------------------------
# File:     webDriverTest.py
# Author:   Anthony Hein
#
# Description: Tests the selenium package by making simple commands.
#-------------------------------------------------------------------------------


from selenium import webdriver

# Environment variables.
from dotenv import load_dotenv
import os

load_dotenv()

wd = webdriver.Chrome(executable_path=os.getenv('DRIVER_PATH'))

wd.get('https://google.com')

search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')

# wd.quit()
