from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Thread

import pandas as pd

df = pd.read_csv("..\CSV's\HouseLinks.csv")

lista = df.values.tolist()

def openDriver(link):
    driver = webdriver.Chrome(keep_alive=True)
    options = Options()
    options.add_argument('--incognito')

    driver.get(link)

def openDriverWithThreads(lista: list):

    threads = [Thread(target=openDriver, args=(link,)) #thread gest the target argument which is the function
                                                       #that will run o the thread and the args argument that defines the arguments of the function.
                                                       #If there is only one arg write a comma afer it, otherwise it will belive it is a tuple of arguments
               for index, link in lista]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
if __name__ == "__main__":
    openDriverWithThreads(lista)