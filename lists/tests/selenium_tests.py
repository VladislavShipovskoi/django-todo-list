from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from lists.models import Todo
from django.contrib.auth.models import User
from selenium import webdriver
from lists.views import (
    REGISTRATION_SUCCESSFUL,
)


class SeleniumUserRegistrationTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(SeleniumUserRegistrationTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumUserRegistrationTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        self.selenium.get(self.live_server_url+"/register")

        selenium.find_element_by_id('id_username').send_keys('newuser')
        selenium.find_element_by_id('id_password1').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('id_password2').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('sign-up-button').click()
        self.assertEqual(REGISTRATION_SUCCESSFUL, self.selenium.find_element_by_id("messages").text)


class SeleniumUserLoginTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(self.live_server_url)
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch34r")
        self.user.save()

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        selenium = self.selenium
        selenium.find_element_by_id("id_username").send_keys("newuser")
        selenium.find_element_by_id("id_password").send_keys("NiGiw3Ch34r")
        selenium.find_element_by_id("sign-in-button").click()

        self.assertEqual(self.user.username, self.selenium.find_element_by_id("username-text").text)