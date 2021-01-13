import time
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from base.tests import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class AdminTestCase(StaticLiveServerTestCase):

	def setUp(self):
		self.base = BaseTestCase()
		self.base.setUp()

		options = webdriver.ChromeOptions()
		options.headless = True
		self.driver = webdriver.Chrome(options=options)
	
		super().setUp()

	def tearDown(self):
		super().tearDown()
		self.driver.quit()

		self.base.tearDown()

	def test_get_visualizerGlobal200(self):
		response = self.client.get(f'{self.live_server_url}/visualizer/global', follow=True)
		self.assertEqual(response.status_code, 200)

	def test_viewVisualizerGlobalLink(self):
		self.driver.get(f'{self.live_server_url}/visualizer/')
		self.driver.set_window_size(1386, 692)
		self.driver.find_element(By.LINK_TEXT, "Visualizar estadisticas globales").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".heading")
		assert len(elements) > 0
		self.driver.close()

	def test_get_visualizerGlobalText(self):
		self.driver.get(f'{self.live_server_url}/visualizer/')
		self.driver.set_window_size(1386, 692)
		self.driver.find_element(By.LINK_TEXT, "Visualizar estadisticas globales").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".heading")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, "p:nth-child(3)")
		assert len(elements) > 0
		self.driver.close()

	def test_visualizerGlobalTable1(self):
		self.driver.get(f'{self.live_server_url}/visualizer/')
		self.driver.set_window_size(1386, 692)
		self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(1)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(2)")
		assert len(elements) > 0
		self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(4)").click()
		self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(3)").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(3)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(4)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(5)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(6)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(7)")
		assert len(elements) > 0
		self.driver.close()


	def test_visualizerGlobalTable2(self):
		self.driver.get(f'{self.live_server_url}/visualizer/')
		self.driver.set_window_size(1386, 692)
		self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(1)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(2)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(3)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(4)")
		assert len(elements) > 0
		self.driver.close()

	def test_visualizerGlobalTable3(self):
		self.driver.get(f'{self.live_server_url}/visualizer/')
		self.driver.set_window_size(1386, 692)
		self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(1)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(2)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(3)")
		assert len(elements) > 0
		elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(4)")
		assert len(elements) > 0
		self.driver.close()