from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome(executable_path=r'C:/Python/chromedriver_win32/chromedriver.exe')

#driver.set_page_load_timeout(10)
driver.implicitly_wait(40)
driver.get('https://fandom.tumblr.com/tagged/week%20in%20review')
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Gestionar opciones'])[1]/following::button[1]").click()

with open('fandometric.txt', 'w') as f:

	consulta  = driver.find_elements_by_css_selector('ol')
	for row in consulta:
		lineas = row.find_elements_by_tag_name("li") 
		for linea in lineas:
			f.write("%s\n" % linea.text)
			#print(linea.text)

time.sleep(10)
#print(consulta)
driver.quit()
