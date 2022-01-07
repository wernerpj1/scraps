from selenium import webdriver

nav = webdriver.Chrome()

nav.get('http://amazon.com')

text = 'jogos playstatio 5'

nav.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(text)
nav.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click
nav.find_element_by_xpath('//*[@id="n/20972797011"]/span/a/span').click

