from lettuce import *
from selenium import webdriver

@before.all
def setup_browser():
  world.browser = webdriver.Chrome('./lib/chromedriver')

@after.all
def teardown_browser(total):
  world.browser.quit()
  print total
  print "Scenarios passed: %d\n Scenarios ran: %d" % (total.scenarios_passed, total.scenarios_ran)

