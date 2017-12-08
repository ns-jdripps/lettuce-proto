from lettuce import *
from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import AssertContextManager
from lettuce import step

@step('The title of the page should become "([^"]*)"')
def the_title_of_the_page_should_become(step, result):
    title = world.browser.title
    try:
        assert_true(step, title == result)
    except AssertionError as e:
        world.browser.quit()
