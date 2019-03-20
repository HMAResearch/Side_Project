from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('/Users/jamescheung/chromedriver')
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def df_cleaner():
raw_df = pd.read_csv('Copy of Definitive MA_JC.csv')

merge = raw_df['News Details'].str.lower().str.contains('merge')
acquire = raw_df['News Details'].str.lower().str.contains('acquire')
sell = raw_df['News Details'].str.lower().str.contains('sell')
sold = raw_df['News Details'].str.lower().str.contains('sold')
partner = raw_df['News Details'].str.lower().str.contains('partner')
join = raw_df['News Details'].str.lower().str.contains('join')
transfer = raw_df['News Details'].str.lower().str.contains('transfer')
member = raw_df['News Details'].str.lower().str.contains('member')

new_df = raw_df[merge | acquire | sell | sold | partner | join | transfer | member]
newer_df = new_df[new_df['DHC News Link'].str.contains('hospital')]


Links = []

Five_df = newer_df.iloc[:5]

for row in Five_df['DHC News Link']:
	Links.append(row)
	# return (Links)

def Get_Text():
	# Links = df_cleaner()
	driver.get('https://www.defhc.com/home/account/login?ReturnUrl=%2Fhome%2F')
	driver.find_element_by_id('MainContent_MainContent_UserName').send_keys('research@hmacademy.com')
	driver.find_element_by_id('MainContent_MainContent_Password').send_keys('Academy1')
	driver.find_element_by_id('MainContent_MainContent_LoginButton').click()

	Final_Text = []
	for url in Links:
		driver.get(url)
		html = driver.page_source

		soup = BeautifulSoup(html, 'html.parser')
		all_text = soup.select('tbody > tr > td')
		Text_List = []
		for text in all_text:
			Text_List.append(text.get_text())
		Final_Text.append(Text_List[4])
		
	return(Final_Text)
Final_Text = Get_Text()
Five_df["Article Text"] = Final_Text

Five_df.to_csv('Integration_Test.csv',encoding='utf-8-sig')

driver.quit()
