from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd


driver = webdriver.Chrome(keep_alive=True)

options = Options()
options.add_argument('--incognito')

driver.get("https://www.storia.ro/ro/rezultate/vanzare/casa/bucuresti?limit=36&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing")

def acceptCookies():
    button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button.click()

def getLinks():    
    list = []
    nextPageButton = driver.find_element(By.XPATH, "//button[@aria-label='Pagina urmatoare']")
    houseList = driver.find_element(By.XPATH, "//div[@data-cy='search.listing.organic']/ul/li[@data-cy='listing-item']")
    while(nextPageButton.is_enabled()):
        houses = houseList.find_elements(By.XPATH, "//a[@data-cy='listing-item-link']")
        for house in houses:
            link = house.get_attribute("href")
            list.append(link)
        nextPageButton.click()
        houseList = driver.find_element(By.XPATH, "//div[@data-cy='search.listing.organic']/ul/li[@data-cy='listing-item']")
        if(driver.find_element(By.XPATH, "//button[@aria-label='Pagina urmatoare']").is_displayed()):
            nextPageButton = driver.find_element(By.XPATH, "//button[@aria-label='Pagina urmatoare']")
        
    df = pd.DataFrame(list)
    df.to_csv("..\CSVs\HouseLinks.csv")

if __name__ == "__main__":
    acceptCookies()
    getLinks()