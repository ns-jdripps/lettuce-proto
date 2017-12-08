# Prototyping UI automation testing

### Uses: 
* Python (https://seleniumhq.github.io/selenium/docs/api/py/api.html)
* Lettuce, ie Cucumber for Python (http://lettuce.it/index.html) 
* Selenium-Python (http://selenium-python.readthedocs.io/index.html)

### How to run (maybe):
1. Clone repo
2. `cd` into the repo
3. Run `python -V`, should ouput something like `Python 2.7.13`
4. Run `pyenv install <python version>`, version must be 2.7.x (Lettuce is not compatible with v3+)
5. Run `pyenv virtual env <python version> lettuce-proto`
6. Run `source activate lettuce-proto`
7. Run `pip install lettuce`
8. Run `pip install -U selenium`
9. Finally, run  `lettuce`

### Test script:
```
Feature: Googling stuff

Scenario: Search NS
  Given I go to "http://www.google.com/"
  When I search "Narrative Science"
  Then the results should contain "Narrative Science | Natural Language Generation Technology"
```

### Step definitions:
```
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
```
### Test result:
![result screenshot](https://github.com/ns-ckao/auto-proto/blob/master/lib/results.png)

### Pros:
* Really easy to get started and write tests.
* 2 dependencies only (Selenium and Lettuce)
* Allows for page objects
* Unrelated to Node

### Cons:
* Not compatible with Python versions 3.x

### Useful reading
* http://selenium-python.readthedocs.io/api.html
* https://the-creative-tester.github.io/Python-Web-Browser-Automation-Lettuce/ (really good)
* https://cucumber.io/docs
* http://seleniumhq.github.io/selenium/docs/api/py/index.html
* http://lettuce.it/tutorial/simple.html#tutorial-simple
* https://help.crossbrowsertesting.com/selenium-testing/frameworks/lettuce/
* http://lettuce.it/reference/terrain.html#reference-terrain (horrific site)
* http://lettuce.it/reference/cli.html#lettuce-including-coverage
* https://pypi.python.org/pypi/selenium


