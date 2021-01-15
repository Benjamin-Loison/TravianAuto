# tool to check which server is the newest among many on gettertools (best way ?)
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

path = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Libs\\geckodriver-v0.28.0-win64\\"

os.chdir(path)
driver = webdriver.Firefox()

getterToolsURL = "https://www.gettertools.com/"
url = getterToolsURL + "fr/"

servers = {}
serversDate = {}

driver.get(url)
elems = driver.find_elements_by_class_name("world")
elemsLen = len(elems)
for elemsIndex in range(elemsLen):
    elem = elems[elemsIndex]
    href = elem.get_attribute('href')
    if not "kingdoms" in href:
        start = elem.get_attribute('data-start')
        startParts = start.split('.')
        day = startParts[0]
        if len(day) == 1:
            day = "0" + day
        startNb = int(startParts[2] + startParts[1] + day)
        name = href.replace(getterToolsURL, "").replace("https://www.getter-tools.de/", "")[:-1] # Deutschland über alles mdr
        nameParts = name.split('.')
        if nameParts[-1].isdigit():
            name = '.'.join(nameParts[:-1])
        #namePartsLen = len(nameParts)
        #if namePartsLen == 5:
        #    name = '.'.join(nameParts[:-1])
        #print(name, start, startNb)
        servers[name] = startNb
        serversDate[name] = start

#print(servers)

serversSortedKeys = sorted(servers, key=servers.get)#, reverse=True)

for key in serversSortedKeys:
    #print(key, serversDate[key])
    try:
        driver.get("https://" + key)
        #print(driver.title)
        elems = driver.find_elements_by_class_name("countdownContent")
        if len(elems) > 0:
            inner = elems[0].get_attribute('innerHTML')
            part = inner.split('<span class="date">')[1].split('</span>')[0].replace('<span class="timezone">', '')

            print(key, serversDate[key], driver.title, part)
            pass
    except WebDriverException:
        pass
        #print("Webpage load failed !")