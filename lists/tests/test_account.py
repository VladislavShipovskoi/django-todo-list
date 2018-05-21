from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from lists.views import (
    REGISTRATION_SUCCESSFUL,
    INVALID_USER_OR_PASSWORD,
    LOGIN_SUCCESSFUL,
    LOGOUT_SUCCESSFUL
)


class UserRegistrationTestCase(LiveServerTestCase):
    """
    UserRegistrationTestCase class tests the registration of the user in the system
    """
    def setUp(self):
        self.selenium = webdriver.Firefox()

    def tearDown(self):
        self.selenium.close()

    def test_registration(self):
        selenium = self.selenium
        self.selenium.get(self.live_server_url+"/registration")
        #act
        selenium.find_element_by_id('id_username').send_keys('newuser')
        selenium.find_element_by_id('id_password1').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('id_password2').send_keys('NiGiw3Ch34r')
        selenium.find_element_by_id('sign-up-button').click()
        #assert
        self.assertEqual(REGISTRATION_SUCCESSFUL, selenium.find_element_by_id("message-text").text)


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
        self.selenium.close()

    def test_login_existing_user(self):
        selenium = self.selenium
        #act
        selenium.find_element_by_id("id_username").send_keys("newuser")
        selenium.find_element_by_id("id_password").send_keys("NiGiw3Ch34r")
        selenium.find_element_by_id("sign-in-button").click()
        #assert
        self.assertEqual(LOGIN_SUCCESSFUL, selenium.find_element_by_id("message-text").text)

    def test_login_non_existing_user(self):
        selenium = self.selenium
        #act
        selenium.find_element_by_id("id_username").send_keys("test")
        selenium.find_element_by_id("id_password").send_keys("test")
        selenium.find_element_by_id("sign-in-button").click()
        #assert
        self.assertEqual(INVALID_USER_OR_PASSWORD, selenium.find_element_by_id("message-text").text)


class UserLogoutTestCase(LiveServerTestCase):
    """

    """
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(self.live_server_url)
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch34r")
        self.user.save()

    def tearDown(self):
        self.selenium.close()

    def test_logout_user(self):
        selenium = self.selenium
        # act
        selenium.find_element_by_id("id_username").send_keys("newuser")
        selenium.find_element_by_id("id_password").send_keys("NiGiw3Ch34r")
        selenium.find_element_by_id("sign-in-button").click()
        selenium.find_element_by_id("logout-button").click()
        # assert
        self.assertEqual(LOGOUT_SUCCESSFUL, selenium.find_element_by_id("message-text").text)