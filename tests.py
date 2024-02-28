from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/login/'
    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][name="uname"][id="fn"][placeholder="Username"].form-control.mt-4')
        email.send_keys("jacob")
        password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"][name="pass"][id="pass"][placeholder="Password"].form-control.mt-4')
        password.send_keys("123")
        print('Typed email and password')
        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-success.mt-4')
        submit.click()
        print('logged in')
        time.sleep(2)

        upslot = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-info')
        upslot.click()
        time.sleep(2)
        print('Updating slot')
        like = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][name="head"][value="kadavanthara"][maxlength="20"][required][id="id_head"]')
        like.send_keys("jacob")
        update=driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-success.mt-4[type="submit"]')
        update.click()
        time.sleep(2)
        print('updated')
        showact=driver.find_element(By.CSS_SELECTOR, 'a.nav-link.m-2[href="/show_activity/"]')
        showact.click()
        bill=driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        bill.click()
        print('showing bill')
        back=driver.find_element(By.CSS_SELECTOR, 'a.navbar-brand.p-3.fs-3.text-white.fw-bold[href="http://127.0.0.1:8000/"]')
        back.click()
        show=driver.find_element(By.CSS_SELECTOR, 'a.nav-link.m-2[href="http://127.0.0.1:8000/data/"]')
        show.click()
        print('showing booking')
        ret=driver.find_element(By.CSS_SELECTOR, 'a.navbar-brand.p-3.fs-3.text-primary.fw-bold[href="http://127.0.0.1:8000/"]')
        ret.click()
        logout = driver.find_element(By.CSS_SELECTOR, 'a.nav-link.m-2[href="http://127.0.0.1:8000/logout/"]')
        logout.click()
        print('logged out')
        
        
        # time.sleep(2)
        # # profile = driver.find_element(By.CSS_SELECTOR, 'a[href="/edit-player-profile"]')
        # # profile.click()
        # # time.sleep(2)
        # # post = driver.find_element(By.CSS_SELECTOR, 'input.form-control[name="loc"]')
        # # post.send_keys("Meenadom")
        # # time.sleep(2)
        # # print('profile updation')
        # # sub = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
        # # sub.click()
        # # time.sleep(2)
        # # print("profile updated")
        # # post = driver.find_element(By.CSS_SELECTOR, 'textarea.form-control[name="feed"]')
        # # post.send_keys("Testing on progress")
        # # time.sleep(2)
        # # testbtn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-warning")
        # # testbtn.click()
        # # print('post created')
        # # time.sleep(2)
        


if __name__ == '__main__':
    import unittest
    unittest.main()