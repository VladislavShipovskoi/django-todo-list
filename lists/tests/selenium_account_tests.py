from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from lists.views import (
    REGISTRATION_SUCCESSFUL,
)


class UserRegistrationTestCase(LiveServerTestCase):
    """
    UserRegistrationTestCase class tests the registration of the user in the system
    """
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(UserRegistrationTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(UserRegistrationTestCase, self).tearDown()

    def test_register(self):
        #arrange
        selenium = self.selenium
        self.selenium.get(self.live_server_url+"/registration")
        #act
        selenium.find_element_by_id('id_username').send_keys('newuser')
        selenium.find_element_by_id('id_password1').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('id_password2').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('sign-up-button').click()
        #assert
        self.assertEqual(REGISTRATION_SUCCESSFUL, self.selenium.find_element_by_id("messages").text)


class UserLoginTestCase(LiveServerTestCase):
    """
    UserLoginTestCase class tests the logged in the system
    """
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(self.live_server_url)
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch34r")
        self.user.save()

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        #arrange
        selenium = self.selenium
        #act
        selenium.find_element_by_id("id_username").send_keys("newuser")
        selenium.find_element_by_id("id_password").send_keys("NiGiw3Ch34r")
        selenium.find_element_by_id("sign-in-button").click()
        #assert
        self.assertEqual(self.user.username, self.selenium.find_element_by_id("username-text").text)