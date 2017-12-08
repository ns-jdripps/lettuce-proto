# Prototyping UI automation testing

### Uses: 
* Python (https://seleniumhq.github.io/selenium/docs/api/py/api.html)
* Lettuce (http://lettuce.it/index.html) 
* Selenium-Python (http://selenium-python.readthedocs.io/index.html)

### To run (maybe):
1. Clone repo
2. `cd` into the repo
3. Run `python -V`, should ouput something like `Python 2.7.13`
4. Run `pyenv install <python version>`, version must be 2.7.x (Lettuce is not compatible with v3+)
5. Run `pyenv virtual env <python version> lettuce-proto`
6. Run `source activate lettuce-proto`
7. Run `pip install lettuce`
8. Run `pip install -U selenium`
9. Finally, run  `lettuce`

![result screenshot](https://github.com/ns-ckao/auto-proto/blob/master/lib/results.png)

### Useful reading
* http://selenium-python.readthedocs.io/api.html
* https://the-creative-tester.github.io/Python-Web-Browser-Automation-Lettuce/
* https://cucumber.io/docs
* http://seleniumhq.github.io/selenium/docs/api/py/index.html
* http://lettuce.it/tutorial/simple.html#tutorial-simple
* https://help.crossbrowsertesting.com/selenium-testing/frameworks/lettuce/
* http://lettuce.it/reference/terrain.html#reference-terrain (horrific site)
* http://lettuce.it/reference/cli.html#lettuce-including-coverage
* https://pypi.python.org/pypi/selenium


