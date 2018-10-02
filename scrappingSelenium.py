from selenium import webdriver
from bs4 import BeautifulSoup

driver =webdriver.Chrome(executable_path = r'C:\Users\akd62\OneDrive\Desktop\chromedriver.exe')

url ='https://www.nba.com/players'
driver.get(url)

soup =BeautifulSoup(driver.page_source,'lxml')

div =soup.find('div',class_='static')
d=div.find_all('a')
for i in d:
    print(i.text)
    print("Player Name: ",i['title'])
    print("More Details:","https://www.nba.com"+i['href'])
    print('')

driver.quit()
