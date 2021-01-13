import time

from authentication.models import UserProfile
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

from voting.models import Voting

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

    def test_viewVisualizerGlobalLink(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.LINK_TEXT, "Visualizar estadisticas globales").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".heading")
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


class List_View_Tests(BaseTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_list_voting_200(self):
        response = self.client.get('/visualizer/')
        self.assertEqual(response.status_code, 200)

    def test_get_votings_from_list_voting_anonymous(self):
        response = self.client.get('/visualizer/')
        votings = response.context['votings']
        self.assertEqual(votings, [])


class Statistics_View_Tests(BaseTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_detail_voting_20(self):
        response = self.client.get('/visualizer/20/statistics')
        self.assertEqual(response.status_code, 200)

    def test_get_detail_voting_404(self):
        response = self.client.get('/visualizer/1010/statistics')
        self.assertEqual(response.status_code, 404)


class Statistics_View_Tests_Selenium(StaticLiveServerTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp()
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        user_admin = UserProfile(username='decide', sex='M', style='N', is_staff=True, is_superuser=True, is_active=True)
        user_admin.set_password('practica1234')
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
        self.base.tearDown()

    def test_statisticsWithLogin(self):
        voting = Voting(name='test 1', desc='r')
        voting.save()
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1920, 1000)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("decide")
        self.driver.find_element(By.ID, "id_password").send_keys("practica1234")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.get(f'{self.live_server_url}/visualizer/1/statistics')
