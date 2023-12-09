from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Thread

import pandas as pd

df = pd.read_csv("..\CSVs\HouseLinks.csv")
linkList = df.values.tolist()

HouseDataList = []
 
def openDriver():

    options = Options()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(keep_alive=True, options=options)

    return driver

def scrapeData(link, driver):

    driver.get(link)
    ok = 1
    try:
        table = driver.find_element(By.XPATH, "//div[@data-testid='ad.top-information.table']")
        tableKeys = table.find_elements(By.XPATH, "//div[contains(@data-cy, 'table-label')]")
        tableValues = table.find_elements(By.XPATH, "//div[contains(@data-testid, 'table-value')] | //button[@data-cy='missing-info-button']")

    except Exception as error:
        print(error)
        ok = 0


    if ok == 1:
        houseDetails = {}

        keys = []
        values = []

        for key in tableKeys:
            keys.append(key.get_attribute("innerText"))
        for value in tableValues:
            values.append(value.get_attribute("innerText"))

        for key in keys:
            for value in values:
                houseDetails[key] = value
                values.remove(value)
                break

        price = driver.find_element(By.XPATH, "//strong[@data-cy='adPageHeaderPrice']")

        houseDetails["Pret"] = price.get_attribute("innerText")

        HouseDataList.append(houseDetails)

def threadWork(linkList, start, noLinks):

    driver = openDriver()

    for i in range(start, noLinks):
        scrapeData(linkList[i][1], driver)

    driver.close()

def openDriverWithThreads(linkList: list):

    size = len(linkList)
    size /= 10
    size = int(size)

    limits = []


    for i in range(0, 10):
        limits.append(size * i)

    limits.append(len(linkList) - 1)

    threads = [Thread(target=threadWork, args=(linkList, limits[i - 1], limits[i])) for i in range(1, 11)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
if __name__ == "__main__":
    openDriverWithThreads(linkList)

    DataSet = pd.DataFrame(HouseDataList)
    DataSet.to_csv(r"..\CSVs\UneditedDataSet--tab-separated.csv", encoding="utf-16", sep='\t')
    DataSet.to_csv(r"..\CSVs\UneditedDataSet.csv", encoding="utf-16")

