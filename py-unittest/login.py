from selenium import webdriver
import unittest

class InstagramLogin(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome('../lib/chromedriver')
    self.browser.get('https://www.instagram.com/accounts/login/')

  def tearDown(self):
    self.browser.quit()

  def testTitle(self):
    self.assertTrue('Instagram' in self.browser.title)

  def testPasswordInputPresent(self):
    self.assertTrue(self.browser.find_element_by_css_selector('input[type="password"]'))

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(InstagramLogin)
  unittest.TextTestRunner(verbosity=2).run(suite)
