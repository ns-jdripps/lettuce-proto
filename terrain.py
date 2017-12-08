from lettuce import *
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
  world.browser = webdriver.Chrome('./lib/chromedriver')

@after.all
def teardown_browser(total):
  world.browser.quit()
  print "Tests passed: %d\n Tests ran: %d" % (total.scenarios_passed, total.scenarios_ran)

