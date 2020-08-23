# Download chromedriver from here: https://chromedriver.chromium.org/downloads
# Specify path of chromedriver in driver varible

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4

try:
	driver=webdriver.Chrome('/home/manik/Downloads/Compressed/chromedriver_linux64/chromedriver')
except Exception as err:
	print("Path of chromedriver not specified. Set path in driver variable.")
	sys.exit()

try:
	print(5+"str1")
	
	# str1="abcde"
	# str[1]='f'

	# list1=[1,2]
	# for i in range(list1):
	# 	print(list[i])

	# Something
	# class Something:
	# 	i=0

	# a=0/0
	# print(a)

	# a=[1]
	# print(a[2])
except Exception as err:
	
	error_caught=str(err)
	print(err)
	
	driver.get("http://google.co.in")
	time.sleep(1)

	#Finds google search box
	box1=driver.find_element_by_name("q")
	time.sleep(1)

	#Searches error on stackoveflow
	search_website="Stackoverflow"
	box1.send_keys(search_website + " python " + error_caught)
	box1.send_keys(Keys.RETURN)
	time.sleep(1)

	#find first link
	link_css="#rso > div > div > div:nth-child(1) > div > div > div.r > a"
	temp=driver.find_element_by_css_selector(link_css)
	temp.click()
	time.sleep(1)

	#find first answer on stackoverflow
	solution_xpath="/html/body/div[5]/div[2]/div/div[1]/div[3]/div[3]/div[2]/div/div[2]/div[1]"
	ab=driver.find_element_by_xpath(solution_xpath)
	print(ab.text)
	



	
	
