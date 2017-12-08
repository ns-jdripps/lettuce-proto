from lettuce import *
from lettuce import step


@step('I go to "([^"]*)"')
def go_to_site(step, url):
    world.browser.get(url)

@step('I search "([^"]*)"')
def input_search_term(step, search_term):
    search_input = world.browser.find_element_by_css_selector(".gsfi")
    search_input.send_keys(search_term)
    search_input.submit()

@step('the results should contain "([^"]*)"')
def results_should_contain(step, result):
    assert world.browser.find_element_by_link_text(result)

@step('I should see "([^"]*)"')
def should_see(step, welcome_text):
    assert world.browser.find_element_by_xpath("//*[text()='%s']" % welcome_text)
