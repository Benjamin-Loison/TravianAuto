#{"Benjamin Loison": "", "Testlouzzd"}

#USERNAME = "Benjamin Loison"
#USERNAME = "Testlouzzd"

#"secret.txt")

from selenium.common.exceptions import NoSuchElementException

#pillages = [[69, -26], [76, -27], [70, -30], [72, -30], [69, -31], ] # [71, -26],

#ActionChains(driver).click(elems[0]).perform()
#
#print(ine)

#driver.find_elements_by_class_name("textButtonV1 green build videoFeatureButton")

#if "textButtonV1 green build videoFeatureButton" in elems[0].get_attribute('innerHTML'):

#elems = driver.find_elements_by_xpath("//*[contains(text(), 'gotoAdventure arrow')]") #driver.find_elements_by_class_name("gotoAdventure arrow")

#[ord(c) for c in s if ord(c) < 128]

"""X = driver.find_elements_by_class_name("coordinateX")
Y = driver.find_elements_by_class_name("coordinateY")
for x, y in zip(X, Y):
    x = toAscii(x.text)
    y = toAscii(y.text)
    #print(type(x))
    x = int(x)
    y = int(y)
    if [x, y] in pillages:
        print("indeed")
    print(x, y)"""

travianAutoPath = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Projects\\TravianAuto\\"
os.chdir(travianAutoPath)

def imp(file):
    file += ".py"
    exec(open(file).read())
    """f = open()
    content = "".join(f.readlines())
    #lines = f.readlines()
    f.close()
    #linesLen = len(lines)
    #for linesIndex in range(linesLen):
    #    line = lines[linesIndex]

        #eval(line)
        #exec(line)
    #print(content)
    #eval(content)
    exec(content)"""

imp("init")
        #print("yes")

        #elem = driver.find_element_by_name("c")
        #ActionChains(driver).click(elem).perform()
        """delay = 3
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'btn_ok')))
            print("Page is ready !")
        except TimeoutException:
            print("Loading took too much time !")"""
        #print(elem, type(elem))
    #print(village)
        #print("!" + village + "!")

        elems = #driver.find_elements_by_class_name("textButtonV1 green build")

pillages["Reblochon"] = [69, -26]
pillages["Juolin"] = [76, -27]
pillages["Miss town"] = [72, -30]

#driver.get(MAP)
driver.get(CARRIERE_D_ARGILE_6)
elems = driver.find_elements_by_xpath("//*[contains(text(), 'textButtonV1 green build')]")
elems = [driver.find_elements_by_id("button5fdd268a6ef54")]
if elems != []:
    elems[0].click()

#driver.get("https://tx3.travian.fr/dorf2.php?a=11&id=21&c=611359")

#RESSOURCES = [195, 189, 193, 190] # WOOD, BRICK, IRON, CEREAL
#PRODUCTION_THEORIQUE = [[], [], [], []]
"""for resIndex in range(4):
    driver.get("http://t4.answers.travian.fr/?view=answers&aid=" + str(RESSOURCES[resIndex]))
    elem = driver.find_element_by_class_name("tbg")
    inner = elem.get_attribute('innerHTML').replace(' style="background-color:#f5f5f5;"', '')
    parts = inner.split("</tr>")
    partsLen = len(parts)
    for partsIndex in range(2, partsLen - 1):
        part = parts[partsIndex]
        partParts = part.split('<td>')
        #print("!" + part + "!")
        partPartsPart = partParts[-1].split("</td>")[0]
        PRODUCTION_THEORIQUE[resIndex] += [int(partPartsPart)]"""
        #print(partPartsPart)
    #print(PRODUCTION_THEORIQUE[resIndex]) # same for all ressources


        #inner = elems[0].get_attribute('innerHTML')
        #print(inner)
        #return False
        #if not "textButtonV1 green new videoFeatureButton disabled" in inner:


        """elems = driver.find_elements_by_class_name("value")
        for elem in elems:
            print(elem.get_attribute('innerHTML'))"""
        """for elem in elems:
            print(elem.get_attribute('innerHTML'))"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


while not build(26, 0, 17):
    pass
toImprove = []

def job1():
    #print("heo")
    while not improve(20, 11):
        #print("success ")
        pass
job1()
"""def job0():
    echo("hey")
    while not build(29, 2, 13):
        echo("checking")
        pass

job0()"""
#wait_start('02:39', lambda: job0())

    """if aid == 194:
        BUILDINGS_COST += [[520, 380, 290, 90], [935, 685, 520, 160], [1685, 1230, 940, 290], [3035, 2215, 1690, 525], [5460, 3990, 3045, 945]]
        continue
    if aid == 188:
        BUILDINGS_COST += [[440, 480, 320, 50], [790, 865, 575, 90], [1425, 1555, 1035, 160], [2565, 2800, 1865, 290], [4620, 5040, 3360, 525]]
        continue
    if aid == 192:
        BUILDINGS_COST += [[200, 450, 510, 120], [360, 810, 920, 215], [650, 1460, 1650, 390], [1165, 2625, 2975, 700], [2100, 4725, 5355, 1260]]
        continue
    if aid == 191:
        BUILDINGS_COST += [[500, 440, 380, 1240], [900, 790, 685, 2230], [1620, 1425, 1230, 4020], [2915, 2565, 2215, 7230], [5250, 4620, 3990, 13015]]
        continue
    if aid == 187:
        BUILDINGS_COST += [[1200, 1480, 870, 1600], [2160, 2665, 1565, 2880], [3890, 4795, 2820, 5185], [7000, 8630, 5075, 9330], [12595, 15535, 9135, 16795]]
        continue
    if aid == 51:
        BUILDINGS_COST += [[130, 160, 90, 40], [165, 205, 115, 50], [215, 260, 145, 65], [275, 335, 190, 85], [350, 430, 240, 105], [445, 550, 310, 135], [570, 705, 395, 175], [730, 900, 505, 225], [935, 1155, 650, 290], [1200, 1475, 830, 370], [1535, 1890, 1065, 470], [1965, 2420, 1360, 605], [2515, 3095, 1740, 775], [3220, 3960, 2230, 990], [4120, 5070, 2850, 1270], [5275, 6490, 3650, 1625], [6750, 8310, 4675, 2075], [8640, 10635, 5980, 2660], [11060, 13610, 7655, 3405], [14155, 17420, 9800, 4355]]
        continue"""

aids = [195, 189, 193, 190, 194, 188, 192, 191, 187, 51, 5, -1, 76, 184, 15, 182, 16, 4, 77, 183, 186, 75, 11, 46, 18, 17, 50, 48, 178, 179, 85, 86, 181, 19, 9, 185, 180, 13, 12, 73, 14, 377, 377, 374, 375]

f = open('buildingsCost.txt', 'w')
f.write(str(BUILDINGS_COST))
f.close()

BUILDINGS_COST = []
aidsLen = len(aids)

for aidsIndex in range(aidsLen): # could save web requests in a file in order not to do them again
    aid = aids[aidsIndex]
    if aid == -1:
        BUILDINGS_COST += [[]] # used to be [] and wasn't working (useful) so
        continue
    driver.get("http://t4.answers.travian.fr/?view=answers&aid=" + str(aid))
    elems = driver.find_elements_by_class_name("tbg")
    if len(elems) > 0:
        elem = elems[0]
    else:
        driver.get("http://t4.answers.travian.fr/?view=toolkit&action=building&gid=" + str(aidsIndex + 1))
        elems = driver.find_elements_by_id("gid" + str(aidsIndex + 1))
        if len(elems) == 0:
            BUILDINGS_COST += [[]]
            continue
        else:
            elem = elems[0]
    inner = elem.get_attribute('innerHTML').replace(' style="background-color:#f5f5f5;"', '').replace("<br>", "")
    parts = inner.split("</tr>")
    partsLen = len(parts)
    BUILDING_COST = []
    for partsIndex in range(2, partsLen - 1):
        part = parts[partsIndex]
        partParts = part.split('<td>')
        cost = [int(partParts[2 + j].split("</td>")[0]) for j in range(4)]
        BUILDING_COST += [cost]
    BUILDINGS_COST += [BUILDING_COST]
    #if aid == 51:
    #    break

"""f = open("buildingsCost.txt", 'w') # could also write directly in the .py but that would be disgusting - let's do it anyway
BUILDINGS_COST_LEN = len(BUILDINGS_COST)
for BUILDINGS_COST_INDEX in range(BUILDINGS_COST_LEN):"""

## one time job - or not (depends whether or not we code data into python)

PRODUCTION_THEORIQUE = []
SPEED = 3

driver.get("http://t4.answers.travian.fr/?view=answers&aid=195")
elem = driver.find_element_by_class_name("tbg")
inner = elem.get_attribute('innerHTML').replace(' style="background-color:#f5f5f5;"', '')
parts = inner.split("</tr>")
partsLen = len(parts)
for partsIndex in range(2, partsLen - 1):
    part = parts[partsIndex]
    partParts = part.split('<td>')
    partPartsPart = partParts[-1].split("</td>")[0]
    PRODUCTION_THEORIQUE += [int(partPartsPart) * SPEED]

RESSOURCES = [195, 189, 193, 190] # WOOD, BRICK, IRON, CEREAL
FARM_COST = [[], [], [], []]#[[]] * 4

for i in range(4):
    driver.get("http://t4.answers.travian.fr/?view=answers&aid=" + str(RESSOURCES[i]))
    elem = driver.find_element_by_class_name("tbg")
    inner = elem.get_attribute('innerHTML').replace(' style="background-color:#f5f5f5;"', '').replace("<br>", "")
    parts = inner.split("</tr>")
    partsLen = len(parts)
    for partsIndex in range(2, partsLen - 1):
        part = parts[partsIndex]
        partParts = part.split('<td>')
        cost = [int(partParts[2 + j].split("</td>")[0]) for j in range(4)]
        #partPartsPart = partParts[2].split("</td>")[0]
        #print(partPartsPart)
        FARM_COST[i] += [cost]

def toSeconds(s):
    #return s
    parts = s.split(':')
    partsInt = [int(part) for part in parts]
    sec = partsInt[2] + partsInt[1] * 60 + partsInt[0] * 3600
    return sec

BUILD_TIME = []#[[]] * 4 # this last doesn't work fine #ref

for i in range(45):
    BUILD_TIME += [[]]
    driver.get("http://t4.answers.travian.fr/?view=toolkit&action=buildingconstructiontimes&speed=3&gid=" + str(i + 1))
    elem = driver.find_element_by_class_name('result')
    inner = elem.get_attribute('innerHTML')
    #print(inner, len(inner))
    #print(len(inner))
    parts = inner.split('<tr>')
    partsLen = len(parts)
    for partsIndex in range(2, partsLen):
        part = toAscii(parts[partsIndex].split('</tr>')[0])
        #print(part)
        partParts = part.split('<td>')
        partPartsLen = len(partParts)
        timeStrs = [partParts[j + 1].split("</td>")[0] for j in range(1, partPartsLen - 1)]
        time = []
        for timeStr in timeStrs:
            if timeStr != "":
                time += [toSeconds(timeStr)]
        BUILD_TIME[i] += [time]
    #break

f = open('buildTime.txt', 'w')
f.write(str(BUILD_TIME))
f.close()

"""actions = ActionChains(driver)
actions.send_keys(Keys.LEFT_CONTROL + 'm')
actions.perform()"""
#ActionChains(driver).key_down(Keys.CONTROL).send_keys('m').key_up(Keys.CONTROL).perform()
"""elem = driver.find_element_by_tag_name('body')
elem.click()
driver.switch_to.active_element().send_keys(Keys.F12)"""
"""action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()"""

"""elems = driver.find_elements_by_class_name("buildingList") # not going to know precisely which slot is already being upgraded...
if len(elems) > 0:

elem = elems[-1]
print(elem.get_attribute('innerHTML'))"""