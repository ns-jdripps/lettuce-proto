from lettuce import *
from lettuce import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

def waitForLoad(selector):
    wait(world.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

@step('I go to "([^"]*)"')
def go_to_site(step, url):
    world.browser.get(url)

@step('I search "([^"]*)"')
def input_search_term(step, search_term):
    search_input_selector = ".gsfi"
    waitForLoad(search_input_selector)
    search_input = world.browser.find_element_by_css_selector(search_input_selector)
    search_input.send_keys(search_term)
    search_input.submit()

@step('the results should contain "([^"]*)"')
def results_should_contain(step, result):
    assert world.browser.find_element_by_link_text(result)

@step('I should see "([^"]*)"')
def should_see(step, welcome_text):
    assert world.browser.find_element_by_xpath("//*[text()='%s']" % welcome_text)


