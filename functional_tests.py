from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:8000')

assert 'Congratulations' in driver.title
