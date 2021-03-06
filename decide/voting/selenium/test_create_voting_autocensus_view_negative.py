# Generated by Selenium IDE
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from base.tests import BaseTestCase
from authentication.models import UserProfile

class TestCreateVotingAutocensusViewNegative(StaticLiveServerTestCase):
  def setUp(self):
    self.base = BaseTestCase()
    self.base.setUp()
    user_admin_superuser = UserProfile(username='adminsuper', sex='F', style='N', is_staff=True, is_superuser=True)
    user_admin_superuser.set_password('qwerty')
    user_admin_superuser.save()
    self.base.user_admin = user_admin_superuser

    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    self.vars = {}
    self.driver.maximize_window() #For maximizing window
    self.driver.implicitly_wait(20) #gives an implicit wait for 20 seconds

    super().setUp() 
  
  def tearDown(self):
    super().tearDown()
    self.driver.quit()

    self.base.tearDown()

  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_create_voting_autocensus_view_negative(self):
    # Test name: test_create_voting_autocensus_view_positive
    # Step # | name | target | value
    # 1 | open | http://localhost:8000/admin/ | 
    self.driver.get(f'{self.live_server_url}/admin/')
    self.driver.find_element_by_id("id_username").send_keys("adminsuper")
    self.driver.find_element_by_id("id_password").send_keys("qwerty")
    self.driver.find_element_by_css_selector("div .submit-row input").click()
    # 3 | click | css=.model-voting .addlink | 
    self.driver.find_element(By.CSS_SELECTOR, ".model-voting .addlink").click()
    # 4 | type | id=id_name | prueba
    self.driver.find_element(By.ID, "id_name").send_keys("pruebacenso")
    # 5 | type | id=id_desc | prueba
    self.driver.find_element(By.ID, "id_desc").send_keys("pruebacenso")
    # 6 | click | css=#add_id_question > img | 
    self.vars["window_handles"] = self.driver.window_handles
    # 7 | storeWindowHandle | root | 
    self.driver.find_element(By.CSS_SELECTOR, "#add_id_question > img").click()
    # 8 | selectWindow | handle=${win70} | 
    self.vars["win70"] = self.wait_for_window(2000)
    # 9 | click | id=id_desc | 
    self.vars["root"] = self.driver.current_window_handle
    # 10 | type | id=id_desc | prueba
    self.driver.switch_to.window(self.vars["win70"])
    # 11 | click | id=id_options-0-number | 
    self.driver.find_element(By.ID, "id_desc").click()
    # 12 | type | id=id_options-0-number | 1
    self.driver.find_element(By.ID, "id_desc").send_keys("pruebacenso")
    # 13 | click | id=id_options-0-option | 
    self.driver.find_element(By.ID, "id_options-0-number").click()
    # 14 | type | id=id_options-0-option | 1
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    # 15 | click | id=id_options-1-number | 
    self.driver.find_element(By.ID, "id_options-0-option").click()
    # 16 | type | id=id_options-1-number | 2
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("1")
    # 17 | click | id=id_options-1-option | 
    self.driver.find_element(By.ID, "id_options-1-number").click()
    # 18 | type | id=id_options-1-option | 2
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    # 19 | click | name=_save | 
    self.driver.find_element(By.ID, "id_options-1-option").click()
    # 20 | close |  | 
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("2")
    # 21 | selectWindow | handle=${root} | 
    self.driver.find_element(By.NAME, "_save").click()
    # 22 | selectWindow | handle=${win245} | 
    # 23 | type | id=id_name | prueba
    self.vars["window_handles"] = self.driver.window_handles
    # 24 | type | id=id_url | http://localhost:8000
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, "#add_id_auths > img").click()
    # 25 | click | name=_save | 
    self.vars["win245"] = self.wait_for_window(2000)
    # 26 | close |  | 
    self.driver.switch_to.window(self.vars["win245"])
    # 27 | selectWindow | handle=${root} | 
    self.driver.find_element(By.ID, "id_name").send_keys("pruebacenso")
    # 28 | click | name=_save | 
    self.driver.find_element(By.ID, "id_url").send_keys("http://localhost:8000")
    # 29 | click | linkText=Home | 
    self.driver.find_element(By.NAME, "_save").click()
    # 30 | click | linkText=Censuss | 
    # 31 | assertText | css=.row1:nth-child(1) a | 1
    self.driver.switch_to.window(self.vars["root"])
    # 32 | assertText | css=.row1:nth-child(1) > .field-voter_id | 1
    self.driver.find_element(By.NAME, "_save").click()
    # self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.get(f'{self.live_server_url}/admin/')
    self.driver.find_element(By.LINK_TEXT, "Censuss").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".paginator").text == "0 censuss"
  
