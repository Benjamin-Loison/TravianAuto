# init

import os, subprocess, time, datetime, threading, requests, math
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt

path = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Libs\\geckodriver-v0.28.0-win64\\"

os.chdir(path)
subprocess.run(["taskkill" ,"/IM", "geckodriver.exe", "/F"])

users = ["Benjamin Loison", "Heieoi"]
playing = "Benjamin Loison"
#server = "https://ts4.travian.fr"
server = "https://tx3.travian.fr" # could link credential to a given server
crendentials = {}

for user in users:
    f = open(user + ".txt")
    PASSWORD = f.readlines()[0]
    crendentials[user] = PASSWORD
    f.close()

TRAVIAN = server + "/"

def page(url):
    return TRAVIAN + url

def php(url):
    return page(url) + ".php"

def building(gid):
    return php("build") + "?gid=" + str(gid)

def id(mid, categ = -1, gid = -1):
    first = True
    midStr = "id=" + str(mid)
    res = php("build")# + "?" + midStr
    if mid != -1:
        res += "?" + midStr
        first = False
    if categ != -1:
        res += "?" if first else "&"
        if first:
            first = False
        res += "category=" + str(categ)
    if gid != -1:
        res += "?" if first else "&"
        if first:
            first = False
        res += "gid=" + str(gid)
    return res

def load(url, t = 1):
    driver.get(VILLAGE1)
    time.sleep(t)

def echo(s):
    now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    print(now + " | " + str(s))

VILLAGE1, VILLAGE2 = php("dorf1"), php("dorf2")
def villageSelect(villageId):
    return "newdid=" + str(villages[villageId])

def VILLAGE1SELECT(villageId):
    return VILLAGE1 + "?" + villageSelect(villageId)

def VILLAGE2SELECT(villageId):
    return VILLAGE2 + "?" + villageSelect(villageId)
MAP = php("karte")

def mapXY(x, y):
    return MAP + "?x=" + str(x) + "&y=" + str(y)

RAPPORTS = page("report")
RASSEMBLEMENT = building(16)
SITUATION = RASSEMBLEMENT + "&tt=1"
ENVOI_DE_TROUPES = RASSEMBLEMENT + "&tt=2"
CARRIERE_D_ARGILE = building(2)
CARRIERE_D_ARGILE_6 = CARRIERE_D_ARGILE + "&id=6"
VILLAGE_BUILD_29 = id(29, 1)
HERO = page("hero")
ADVENTURES = HERO + "/adventures"

pillages = {}
pillages["fiodor"] = [71, -26]

def cookies():
    elemNotFound = True
    while elemNotFound:
        #print("here")
        try:
            #elem = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll") # Decline
            #elem = driver.find_element_by_class_name("cmpboxbtn cmpboxbtnno")
            elem = driver.find_element_by_id("cmpwelcomebtnno")
            elemNotFound = False
        except NoSuchElementException:
            #print("not found")
            pass
        #if elemNotFound:
        time.sleep(1)
    #ActionChains(driver).click(elem).perform()
    elem.click()

driver = webdriver.Firefox()
# mute audio "doesn't seem possible" with Firefox in Python... - can't find a way to make it work

driver.get(VILLAGE1)

#cookies() # should set a timeout

#time.sleep(2)
elem = driver.find_element_by_name("name")
elem.send_keys(playing)
elem = driver.find_element_by_name("password")
elem.send_keys(crendentials[playing])
elem.send_keys(Keys.RETURN)

time.sleep(1)

GID_WOOD, GID_BRICK, GID_IRON, GID_CEREAL = 1, 2, 3, 4

# TODO: warning the following decleration depends on village production ressource repartition...
WOODS, BRICKS, IRONS, CEREALS = [1, 3, 14, 17], [5, 6, 16, 18], [4, 7, 10, 11], [2, 8, 9, 12, 13, 15]
RESSOURCES_FARMS = [WOODS, BRICKS, IRONS, CEREALS]
farms = {}#{1: GID_WOOD, 3: GID_WOOD, 14: GID_WOOD, 17: GID_WOOD,
#2: GID_CEREAL, 8}
for ELEMS, GID in zip([WOODS, BRICKS, IRONS, CEREALS], [GID_WOOD, GID_BRICK, GID_IRON, GID_CEREAL]):
    for elem in ELEMS:
        farms[elem] = GID

def toAscii(s):
    return s.replace('(', '').replace(')', '').replace('\u202c', '').replace('\u202d', '').replace('\n', "").replace(" ", "").replace('−', '-').replace('\t', '')

natureNames = ["rat", "araignée", "serpent", "chauve-souris", "sanglier", "loup", "ours", "crocodile", "tigre", "éléphant"]
natureDef = [[25, 20], [35, 40], [40, 60], [66, 50], [70, 33], [80, 70], [140, 200], [380, 240], [170, 250], [440, 520]]
natureDefAverage = []
for natureD in natureDef:
    #cavalerie, infanterie = natureD
    natureDefAverage += [sum(natureD) / len(natureD)]

# 1-1-1-15 finder ? - done

travianAutoPath = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Projects\\TravianAuto\\"
os.chdir(travianAutoPath)

def evalFile(file):
    #file += ".py"
    return eval(open(file).read())

PRODUCTION_THEORIQUE = evalFile("productionTheorique.txt")

FARM_COST = evalFile("farmCost.txt")
BUILD_TIME = evalFile("buildTime.txt") # used to be FARM_TIME

DERIVATIVES = []
X = list(range(20))
for i in range(4):
    D = []
    previousProductionTheorique = 0
    for j in range(20):
        D += [round(100 * (PRODUCTION_THEORIQUE[j] - previousProductionTheorique) / sum(FARM_COST[i][j]), 2)]
        previousProductionTheorique = PRODUCTION_THEORIQUE[j]
    DERIVATIVES += [D]

    #plt.plot(X, D, label=str(i))

#plt.legend(loc="upper right")
#print(DERIVATIVES)
#plt.show()

#

driver.get(VILLAGE1)
villages = [] # could also use a dict
villagesCoo = []
#elems = driver.find_elements_by_xpath("//*[contains(text(), 'newdid')]")
elem = driver.find_element_by_id("sidebarBoxVillagelist")
inner = elem.get_attribute('innerHTML')
#print(inner)
parts = inner.split('href="?newdid=')
partsLen = len(parts)
for partsIndex in range(1, partsLen):
    part = parts[partsIndex].split('&')[0]
    #print(part)
    villages += [int(part)]

villagesLen = len(villages)

elemsX = driver.find_elements_by_class_name("coordinateX")
elemsY = driver.find_elements_by_class_name("coordinateY")
elemsLen = len(elemsX)
for elemsIndex in range(elemsLen):
    elemX, elemY = elemsX[elemsIndex], elemsY[elemsIndex]
    xStr, yStr = toAscii(elemX.get_attribute('innerHTML')), toAscii(elemY.get_attribute('innerHTML'))
    x, y = int(xStr), int(yStr)
    #print(x, y)
    villagesCoo += [[x, y]]

WOOD, BRICK, IRON, CEREAL = 0, 1, 2, 3

currentRessources, production, currentDepots = {}, {}, {} # I was planning to use another function for depots but here it is the same complexity etc so let's do it

def initResAndProd(villageId):
    currentRessources[villageId], production[villageId] = [0] * 4, [0] * 4
    driver.get(VILLAGE1SELECT(villageId))
    for i in range(4):
        elem = driver.find_element_by_id("l" + str(i + 1))
        inner = toAscii(elem.get_attribute('innerHTML'))
        #print(inner, type(inner), inner[1])
        currentRessources[villageId][i] = int(inner)

    #print(currentRessources)

    elem = driver.find_element_by_id("production")
    content = elem.get_attribute('innerHTML')
    #print(content)
    parts = content.split('<td class="num">')
    for i in range(4):
        production[villageId][i] = int(toAscii(parts[i + 1].split('</td>')[0]))

    # the adjective "medium" let's think that this might change... (could go on level up in DOM to solve this problem)

    #time.sleep(1)
    elem = driver.find_element_by_class_name("warehouse")#"warehouse_medium")
    inner = elem.get_attribute('innerHTML')
    #print(inner)
    depot = int(toAscii(inner.split('value">')[1].split('</div>')[0]))

    elem = driver.find_element_by_class_name("granary")#_medium")
    inner = elem.get_attribute('innerHTML')
    silo = int(toAscii(inner.split('value">')[1].split('</div>')[0]))

    currentDepots[villageId] = [depot, silo]

#initResAndProd()

#print(production)

"""driver.get(SITUATION)
innerAt, innerButin = None, None
elemAt = driver.find_elements_by_class_name("at")
if elemAt != []:
    innerAt = elemAt[0].get_attribute('innerHTML').replace('<span>à&nbsp;', '').split('</span>')[0] # does Travian absolutely support well one day to the other ?
    elemRes = driver.find_elements_by_class_name("res") # not coded for multiple butin at the same time
    if elemRes != []:
        innerButin = elemRes[0].get_attribute('innerHTML')"""

def resAtTime(villageId, a):
    b = datetime.datetime.now()#datetime(1970, 1, 1)
    s = (a-b).total_seconds()
    if s >= 0:
        ressourcesAtTime = [currentRessources[villageId][i] + int(production[villageId][i] * s / 3600) for i in range(4)]
        """if innerButin is not None:
            comeBackTime = datetime.datetime.strptime("12 20 " + innerAt + " 2020 GMT", "%m %d %H:%M:%S %Y %Z")
            if (a - comeBackTime).total_seconds() >= 0:
                #print("added")

                parts = innerButin.split('<span class="value ">')
                for i in range(1, 5):#len(parts)):
                    part = parts[i]
                    ressource = int(part.split('</span>')[0])
                    #print(ressource)
                    #print(i, ressource)
                    ressourcesAtTime[i - 1] += ressource"""

        return ressourcesAtTime
    return None

"""tim = datetime.datetime.strptime("12 20 03:46:44 2020 GMT", "%m %d %H:%M:%S %Y %Z")
ressourcesAtTime = resAtTime(tim)
print(ressourcesAtTime)"""

# palais: no gold and no fast video (need to make this case in my algo) cf build function ?

# WHEN THIS AMOUNT OF RESSOURCES ?

def getTimeWhenEnoughRes(villageId, neededRessources):
    initResAndProd(villageId)
    s = 0
    #noStop = True
    while True:#noStop:
        tim = datetime.datetime.now() + datetime.timedelta(seconds = s)
        #print(tim)
        ress = resAtTime(villageId, tim)
        if ress is None:
            return None, None, 0
        for i in range(4):
            if ress[i] < neededRessources[i]:
                break
            if i == 3:
                #noStop = False
                #print(tim, ress, s)
                return tim, ress, s

        #if ress is not None:
        #    print(tim, ress)
        s += 1

neededRessources = [730, 900, 505, 225] # should only give building (slot) id
#print(getTimeWhenEnoughRes(neededRessources))

def getTimeWhenSumEnoughRes(neededRes):
    s = 0
    while True:
        tim = datetime.datetime.now() + datetime.timedelta(seconds = s)
        ress = resAtTime(tim)
        if sum(ress) >= neededRes:
            return tim, ress, s
        s += 1

#print(getTimeWhenSumEnoughRes(60000))

# current fields (want to get first available upgrade and the upgrade which would involve the best production)

# bunch of code was designed for a single village and not multi villages
CURRENT_FARMS = []#[[]] * villagesLen # not [[] * villagesLen]
for i in range(villagesLen):
    CURRENT_FARMS += [[]]

def loadFarmsLevelVillage(villageId):
    CURRENT_FARMS[villageId] = []
    driver.get(VILLAGE1SELECT(villageId))
    elems = driver.find_elements_by_class_name("labelLayer")
    elemsLen = len(elems)
    for elemsIndex in range(elemsLen):
        elem = elems[elemsIndex]
        inner = elem.get_attribute('innerHTML')
        #print(elemsIndex + 1, inner)
        CURRENT_FARMS[villageId] += [int(inner)] # pay attention to indices when accessing this

def loadFarmsLevel(): # not really used for the moment
    for villageId in range(villagesLen):
        loadFarmsLevelVillage(villageId)

#

"""bestS, bestId = None, None
CURRENT_FARMS_LEN = len(CURRENT_FARMS)
for farmIndex in range(CURRENT_FARMS_LEN):
    farmLevel = CURRENT_FARMS[farmIndex]
    farmIndex += 1 # shouldn't involve troubles from one loop to the other
    farmType = 0
    if farmIndex in BRICKS:
        farmType = 1
    elif farmIndex in IRONS:
        farmType = 2
    elif farmIndex in CEREALS:
        farmType = 3
    needRes = FARM_COST[farmType][farmLevel]
    _, _, s = getTimeWhenEnoughRes(needRes)
    #print(s, farmType, farmLevel, needRes)
    if bestS is None or s < bestS:
        bestS = s
        bestId = farmIndex"""
"""print(bestS, bestId, CURRENT_FARMS[bestId - 1])

maxFarmIndex = max(CURRENT_FARMS) # could also use min here to check low investments, should use ratio (production/ressources needed)
maxDeltaFarm = PRODUCTION_THEORIQUE[maxFarmIndex] - PRODUCTION_THEORIQUE[maxFarmIndex - 1]
deltaMoulin = int(0.05 * production[3])
print("local derivative, invest in:")
print("moulin" if deltaMoulin > maxDeltaFarm else "farm")"""
# should compute a derivative considering needed ressources

#

def build(mid, categ, buildingId):
    driver.get(id(mid, categ))
    time.sleep(1)
    elems = driver.find_elements_by_class_name("contractLink")
    for elem in elems:
        ine = elem.get_attribute('innerHTML')
        if "?a=" + str(buildingId) in ine:
            url = ine.split("window.location.href = '")[1].split("'")[0].replace("&amp;", "&")
            finalURL = TRAV + url
            print(finalURL)
            driver.get(finalURL)
            return True
    return False

oasis = [[4, -52]]

def improve(mid, gid, t, villageId = 0):
    #driver.get(VILLAGE1SELECT(villageId))
    #time.sleep(t)
    url = id(mid, -1, gid) + "&" + villageSelect(villageId)
    #print(url)
    driver.get(url) # not building, last argument isn't necessary in this case
    time.sleep(t) # should make a version without sleep but waiting when button is available
    elems = driver.find_elements_by_xpath("//*[contains(text(), 'plus vite')]")
    if elems != []:
        if elems[0].get_attribute("class") == "textButtonV1 green build videoFeatureButton":
            elems[0].click()
            # doesn't seem to need a time.sleep here
            while len(driver.find_elements_by_id("dialogContent")) > 0:
                #print("waiting")
                time.sleep(1)
            #print("returned !")
            return True
    return False

"""toImproveV0 = [[29, 10], [20, 11]]
toImproveV1 = [[29, 11], [31, 10]]"""
toImproves = [[[20, 11], [29, 10], [29, 10], [24, 37], [24, 37], [24, 37], [24, 37]], [[29, 11], [29, 11], [31, 10], [34, 6], [37, 5]], [[31, 11], [31, 11], [29, 10], [6, 2], [7, 3], [11, 3]]]
"""toImprove = []
improveFarms = [7, 4, 14, 8, 9, 12, 13, 15, 2]
for improveFarm in improveFarms:
    toImprove += [[improveFarm, farms[improveFarm]]]"""

def runImprove(toImproves):
    #toImprovesLen = len(toImproves) # let's assume for the moment that all villages have equal number of buildings to build in queue - well doesn't work fine even if assume this
    """toImproveLen = len(toImprove)
    for toImproveIndex in range(toImproveLen):
        imp = toImprove[toImproveIndex]
        echo("Waiting for: " + str(imp))
        while not improve(imp[0], imp[1], 15, villageId): # could compute locally when it will happend ?
            #print("Improving: ", imp)
            pass
        if toImproveIndex != toImproveLen - 1:
            time.sleep(60) # max pub length ?
    """
    #for i in range(toImprovesLen):
    echo("Going to improve things...")
    i = 0
    while toImproves != []:
        toImprove = toImproves[i]
        if toImprove != []:
            imp = toImprove[0]
            if improve(imp[0], imp[1], 15, i):
                echo(str(imp) + " at village " + str(i) + " built !")
                del toImprove[0] # does imp also work here ?
                time.sleep(60)
        else:
            del toImproves[i]
        i += 1
        if toImproves != []: # otherwise divise by 0
            i = i % len(toImproves)
    echo("Finish running all improvements")

runImprove(toImproves)
#runImprove(toImproveV0, 0) # using two python shells doesn't seem to work fine with "firefox driver" implementation of Selenium
#runImprove(toImproveV1, 1)
# could be cool to make a tool to check if not loosing ressources because of too much...

"""elemsLen = 1
while elemsLen > 0:
    driver.get(ADVENTURES)
    elems = driver.find_elements_by_xpath("//*[contains(text(), 'Débuter')]")
    elemsLen = len(elems)
    if elemsLen != 0:
        elems[0].click()
    time.sleep(15)"""

def wait_start(runTime, action):
    startTime = datetime.time(*(map(int, runTime.split(':'))))
    while startTime > datetime.datetime.today().time():
        time.sleep(1)
    return action()

#wait_start('03:46', runImprove)

# TODO: should do a while true loop doing raids, aventures, buildings...

# threads require multi drivers ?
"""l = []

noStopThread = True
def threadFunction():
    global l, noStopThread
    while noStopThread:
        #print("hey")
        if len(l) > 0:
            del(l[0])
        print(l)
        time.sleep(1)

x = threading.Thread(target=threadFunction)
x.start()"""

"""def clickOnMiddleMap():
    elem = driver.find_element_by_id("mapContainer")
    action = ActionChains(driver)
    action.move_to_element_with_offset(elem, 250, 200)
    action.click()
    action.perform()

driver.get(MAP)
clickOnMiddleMap()

#elem = driver.find_element_by_class_name("coordinates coordinatesWrapper") # I believe this doesn't work on span markup
elem = driver.find_element_by_class_name('titleInHeader')
inner = elem.get_attribute('innerHTML')
#print(inner)
parts = inner.split('"coordinateX">(')
if len(parts) >= 2:
    VILLAGE_X = int(toAscii(parts[1].split('</span>')[0]))
    VILLAGE_Y = int(toAscii(inner.split('"coordinateY">')[1].split(')</span>')[0]))
VILLAGE_X, VILLAGE_Y = 3, -51"""
cages = 100
# checking whole map is too heavy because 400 * 400 = 160 000 (but is it the same map on every server :O ? - no it's different (at least between fr4 and frx3))
# so looking for a specific things circularly ? (but perfect might not be found :/)

def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

def distanceVillages(villageId0, villageId1):
    x0, y0 = villagesCoo[villageId0]
    x1, y1 = villagesCoo[villageId1]
    return distance(x0, y0, x1, y1)

treated, oasis, emptyOasis = 0, 0, 0
# curl section

# could also think about doing with multiple oasis, threading and C++? could optimize

if False:
    driver.get(MAP)

    cookies_list = driver.get_cookies()
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    #cookies_dict['Content-Type'] = # why executed even if False :'(

    print(cookies_dict)

    AJAX = TRAVIAN + 'api/v1/ajax/'
    #headers = cookies_dict
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ', 'Cookie': '__cmpcc=1; JWT='} # autorization value update doesn't seem so important

    def get(x, y):
        url = AJAX + 'mapPositionData'
        payload = '{"data":{"x":' + str(x) + ',"y":' + str(y) + ',"zoomLevel":3,"ignorePositions":[]}}'
        r = requests.post(url, data=payload, headers=headers) # could make a function for this
        return r.text

    def lis(x, y):
        global l
        if x < MIN_X or x >= MAX_X or y < MIN_Y or y >= MAX_Y:
            return
        res = get(x, y)
        if "login" in res:
            raise Exception('need to login lis')
        parts = res.split('position":{"x":"')
        partsLen = len(parts)
        for partsIndex in range(1, partsLen):
            part = parts[partsIndex]
            #xStr, yStr = part.split('"')[0], part.split('y":"')[1].split('"')[0]
            xStr = part.split('"')[0]
            #print(part)
            yStr = part.split('y":"')[1].split('"')[0]
            x, y = int(xStr), int(yStr)
            pair = [x, y]
            if "%" in part:
                #print(x, y)
                #l += [pair]
                if not pair in l:
                    #print(x, y)
                    l += [pair]
            """if pair in l:
                print("already in") # no problem with doublons here - mhh let's check in order to manage also borders
            else:
                l += [pair]"""
        #return res

    # unzoom = :galaxy_brain:
    # might have some troubles with borders with this approach
    titles = []
    titlesWithCoo = {}
    l = []
    #reqs = 0
    ccD = 10 ** 5
    ccX, ccY = 0, 0
    MIN, MAX, STEP_X, STEP_Y = -200, 201, 30, 30
    STEP_X_2, STEP_Y_2 = STEP_X // 2, STEP_Y // 2
    MIN_X, MIN_Y, MAX_X, MAX_Y = MIN, MIN, MAX, MAX # MIN + STEP_X_2, MIN + STEP_Y_2, MAX - STEP_X_2, MAX - STEP_Y_2
    for x in range(MIN_X, MAX_X, STEP_X):
        for y in range(MIN_Y, MAX_Y, STEP_Y):
            #print(x, y)
            #lis(x, y)
            res = get(x, y)
            #print(res)
            parts = res.split('position":{"x":"')
            #parts = res.split('"title":"')
            partsLen = len(parts)
            for partsIndex in range(1, partsLen):
                part = parts[partsIndex]
                xStr = part.split('"')[0]
                yStr = part.split('y":"')[1].split('"')[0]
                x, y = int(xStr), int(yStr)
                #print("!", part, "!")
                partParts = part.split('"title":"')
                if len(partParts) < 2:
                    continue
                part = partParts[1]
                title = part.split('"')[0]
                if "{k.f6}" in title:
                    d = distance(VILLAGE_X, VILLAGE_Y, x, y)
                    if d < ccD:
                        ccD = d
                        ccX, ccY = x, y
                        print(ccD, ccX, ccY)
                    continue
                if "{k.dt}" in title:
                    continue
                #print(title)
                if not title in titles:
                    titles += [title]
                    titlesWithCoo[title] = [x, y]
            """pair = [x, y]
            if pair in l:
                print("already in")
            else:
                l += [pair]"""
            #reqs += 1
            #break
        #break
    #print(reqs)
    for title in titles:
        print(title)

    for title in titlesWithCoo:
        print(title, titlesWithCoo[title])

    def req(x, y):
        url = AJAX + 'viewTileDetails'
        payload = '{"x":' + str(x) + ',"y":' + str(y) + '}'
        r = requests.post(url, data=payload, headers=headers)
        res = r.text
        #print(res)
        if "login" in res:
            raise Exception('need to login req')
        return res

    """startTime = time.time()
    res = req(50, 50)
    endTime = time.time()
    print(endTime - startTime)"""#, res)
    # 0.135 s

    bestDefCages, bestX, bestY = 0, 0, 0
    bestCageRepartition = []

    def product(X, Y):
        return sum([x * y for x, y in zip(X, Y)])

    ANIMALS_NB = 10
    #cages = 9

    def getCageRepartition(troops):
        cagesRemaining = cages
        cagesRepartition = [0] * ANIMALS_NB
        while cagesRemaining > 0:
            for troopsIndex in range(ANIMALS_NB):
                troop = troops[troopsIndex]
                if troop > 0:
                    troops[troopsIndex] -= 1
                    cagesRepartition[troopsIndex] += 1
                    cagesRemaining -= 1
                    #print(cagesRemaining)
                    if cagesRemaining == 0:
                        break
        return cagesRepartition

    #reqs = 0
    skip = False
    def workXY(x, y):
        #global reqs
        global bestDefCages, bestCageRepartition, skip, l, bestX, bestY
        #echo(str([x, y]))
        """if x == 131 and y == 63:
            echo("Gonna work")
            skip = False"""
        if not [x, y] in l:
            #print([x, y])
            return
        if skip:
            return
        #echo("Working...")
        res = req(x, y)
        #reqs += 1
        if "Oasis inoccup" in res:
            if "aucun" in res:
                return
            #print("Working on", x, y)
            troopsStr = res.split('amounts\\":{\\"')[1].split('}')[0]
            parts = troopsStr.split(',\\"')
            partsLen = len(parts)
            troops = [0] * ANIMALS_NB
            for partsIndex in range(partsLen):
                part = parts[partsIndex]
                partParts = part.split('\\":')
                #print(part, partParts)
                animalId = int(partParts[0]) - 1
                amount = int(partParts[1])
                troops[animalId] = amount
            defAmount = product(troops, natureDefAverage)
            if sum(troops) <= cages:
                defCages = defAmount
                cageRepartition = troops
            else:
                cageRepartition = getCageRepartition(troops)
                defCages = product(cageRepartition, natureDefAverage)
            if defCages > bestDefCages:
                bestDefCages = defCages
                bestCageRepartition = cageRepartition
                bestX = x
                bestY = y
            echo(str(["oasis not occupied found at ", bestDefCages, defCages, x, y, bestX, bestY]))

    d = 1
    while bestDefCages < natureDefAverage[-1] * cages:
        for x in range(VILLAGE_X - d, VILLAGE_X + d + 1):
            workXY(x, VILLAGE_Y - d)
            workXY(x, VILLAGE_Y + d)
        for y in range(VILLAGE_Y - d + 1, VILLAGE_Y + d):
            workXY(VILLAGE_X - d, y)
            workXY(VILLAGE_X + d, y)
        #break
        d += 1

    #
    def checkXY(x, y):
        global treated, oasis, emptyOasis
        driver.get(mapXY(x, y))
        clickOnMiddleMap()
        time.sleep(1)
        elems = driver.find_elements_by_class_name("titleInHeader")
        if elems != []:
            inner = elems[0].get_attribute('innerHTML')
            #print(inner, len(elems))
            if "Oasis" in inner:
                #print("there")
                oasis += 1
                inner = driver.find_element_by_id("troop_info").get_attribute('innerHTML')
                if "aucun" in inner:
                    print("found", x, y, distance(VILLAGE_X, VILLAGE_Y, x, y))
                    emptyOasis += 1
                    #time.sleep(10)
        treated += 1

    # could use simulateur de combat to check if no troop lose even if there are some nature troops
    d = 1
    while True: # shouldn't stop on first "yes" because might have a less distance "yes"
        print(d, treated, oasis, emptyOasis)
        # this approach is bad because we are going to consider many times the same center area
        """for y in range(VILLAGE_Y - d, VILLAGE_Y + d + 1):
            for x in range(VILLAGE_X - d, VILLAGE_X + d + 1):
                checkXY(x, y)"""
                #time.sleep(3)
        for x in range(VILLAGE_X - d, VILLAGE_X + d + 1):
            checkXY(x, VILLAGE_Y - d)
            checkXY(x, VILLAGE_Y + d)
        for y in range(VILLAGE_Y - d + 1, VILLAGE_Y + d):
            checkXY(VILLAGE_X - d, y)
            checkXY(VILLAGE_X + d, y)
        d += 1

# situation troops

if False:
    PILLAGE_MSG = USERNAME + " pille "
    ATTACK_MSG = USERNAME + " attaque "

    driver.get(SITUATION)
    alreadyAttacked = []
    attacks = driver.find_elements_by_class_name("troopHeadline")
    for attack in attacks:
        village = attack.get_attribute('innerHTML')
        villageParts = village.split(ATTACK_MSG)
        if len(villageParts) >= 2:
            village = villageParts[1].split('\t')[0]
            alreadyAttacked += [village]

# analyse pop alliances in 50 cases range ? - let's display villages of players on graph instead and if could have have labels with pop it would be perfect

if False:
    driver.get(VILLAGE2SELECT(0))
    driver.get(id(32, 18))
    elem = driver.find_element_by_id("findAlliance")
    inner = elem.get_attribute('innerHTML')
    parts = inner.split('href="/alliance/')
    alliances, alliancesNames = [], []
    partsLen = len(parts)
    for partsIndex in range(1, partsLen):
        part = parts[partsIndex]
        alliance = part.split('"')[0]
        #print(alliance)
        alliances += [alliance]

    parts = inner.split('title="">')
    partsLen = len(parts)
    for partsIndex in range(1, partsLen):
        part = parts[partsIndex]
        allianceName = part.split('</a>')[0]
        #print(alliance)
        alliancesNames += [allianceName]

    for alliance, allianceName in zip(alliances, alliancesNames):
        #print(alliance, allianceName)
        url = TRAVIAN + "alliance/" + alliance + "/profile?st=members"
        X, Y = [], []
        driver.get(url)
        #plt.scatter(X, Y)
        elem = driver.find_element_by_class_name("allianceMembers")
        inner = elem.get_attribute("innerHTML")
        profiles = []
        parts = inner.split('/profile/')
        partsLen = len(parts)
        for partsIndex in range(1, partsLen):
            part = parts[partsIndex]
            profile = part.split('"')[0]
            profiles += [profile] # could directly do job here
            #print(profile)
        profilesLen = len(profiles)
        for profilesIndex in range(profilesLen):
            profile = profiles[profilesIndex]
            url = TRAVIAN + "profile/" + profile
            driver.get(url)
            pops, xs, ys = [], [], []
            elem = driver.find_element_by_id("villages")
            inner = elem.get_attribute('innerHTML')
            parts = inner.split('inhabitants">')
            partsLen = len(parts)
            for partsIndex in range(1, partsLen):
                part = parts[partsIndex]
                pop = toAscii(part.split('</td>')[0])
                #print("@" + pop + "@")#, "!" + part + "!")
                pops += [pop]
                #break
            elems = driver.find_elements_by_class_name("coords")
            for elem in elems:
                inner = elem.get_attribute('innerHTML')
                """partsX = inner.split('coordinateX">(')
                partsY = inner.split('coordinateY">')
                partsLen = len(partsX)
                for partsIndex in range(partsLen):
                    part = parts[partsIndex]
                    partX, partY = partsX[partsIndex], partsY[partsIndex]
                    x = partX.split('</span>')[0]
                    y = partY.split(')')[0]
                    print(x, y)
                break"""

            break
        #break

    plt.show()

# show my alliance

# copied from above
if False:
	# url = "https://tx3.travian.fr/alliance/17/profile?st=members"
    url = TRAVIAN + "alliance/profile?st=members"
    X, Y = [], []
    driver.get(url)
    elem = driver.find_element_by_class_name("allianceMembers")
    inner = elem.get_attribute("innerHTML")
    profiles = []
    parts = inner.split('/profile/')
    partsLen = len(parts)
    for partsIndex in range(1, partsLen):
        part = parts[partsIndex]
        profile = part.split('"')[0]
        profiles += [profile]
    fig, ax = plt.subplots()
    profilesLen = len(profiles)
    for profilesIndex in range(profilesLen):
        profile = profiles[profilesIndex]
        url = TRAVIAN + "profile/" + profile
        driver.get(url)
        name = driver.find_element_by_class_name("titleInHeader").get_attribute('innerHTML')
        pops, xs, ys = [], [], []
        elem = driver.find_element_by_id("villages")
        inner = elem.get_attribute('innerHTML')
        parts = inner.split('inhabitants">')
        villagesNb = len(parts)
        for partsIndex in range(1, villagesNb):
            part = parts[partsIndex]
            pop = toAscii(part.split('</td>')[0])
            #print("@" + pop + "@")#, "!" + part + "!")
            pops += [pop]
            #break
        elems = driver.find_elements_by_class_name("coords")
        for elem in elems:
            inner = elem.get_attribute('innerHTML')
            partsX = inner.split('coordinateX">(')
            partsY = inner.split('coordinateY">')
            partsLen = len(partsX)
            for partsIndex in range(1, partsLen):
                part = parts[partsIndex]
                partX, partY = partsX[partsIndex], partsY[partsIndex]
                x = toAscii(partX.split('</span>')[0])
                y = toAscii(partY.split(')')[0])
                #print("!", x, "!", y, "!")
                xs += [int(x)]
                ys += [int(y)]
            #break
        #plt.scatter(xs, ys)
        ax.scatter(xs, ys)

        for i, txt in enumerate(pops):
            ax.annotate(name + " (" + str(i + 1) + "/" + str(villagesNb) + ", " + txt + ")", (xs[i], ys[i]))
        #break

    plt.show()

# end show my alliance

# pillage

if False:
    for pillage in pillages:
        if not pillage in alreadyAttacked:
            driver.get(ENVOI_DE_TROUPES)
            x, y = pillages[pillage]

            driver.find_element_by_css_selector("input[type='radio'][value='3']").click() # 4 for pillage but auto defense ?! - yes

            elem = driver.find_element_by_name("troops[0][t1]")
            elem.send_keys(str(2))

            elem = driver.find_element_by_name("x")
            elem.send_keys(str(x))
            elem = driver.find_element_by_name("y")
            elem.send_keys(str(y))

            elem.send_keys(Keys.RETURN)

            time.sleep(1)
            elem = driver.find_elements_by_class_name("error")
            if len(elem) != 0:
                print(pillage + " is under beginning protection !")
                continue

            elem = driver.find_element_by_id("btn_ok")
            elem.click()

# grow from scratch (let's first not do optimized but just automatic as quick as possible #HumanCanSleep)

if False:
    def remove(l0):
        for i in range(4):
            ressources[i] -= l0[i]

    def state():
        print(timing, ressources, production, cerealConsumptionRemaining)

    def add(timeDelta):
        global timing
        timing += timeDelta
        factor = factorRes * timeDelta / 3600
        for i in range(4):
            ressources[i] += int(production[i] * factor)

    timing = 0
    factorRes = 1
    #serverSpeed = 3
    ressources = [750] * 4
    production = [58, 52, 48, 56, 20]
    cerealConsumptionRemaining = 20

    # building Fer 1
    cerealConsumptionRemaining -= 3
    remove([100, 80, 30, 60])
    state()

    # building Bucheron 1
    cerealConsumptionRemaining -= 2
    remove([40, 100, 50, 60])
    state()

    # finished building Fer 1
    add(150)
    production[2] += 12
    state()
    factorRes = 1.25

    # building Argile 1
    cerealConsumptionRemaining -= 2
    remove([80, 40, 80, 50])
    state()

    # finished building Bucheron 1
    add(90)
    production[0] += 12
    state()

    # building Cereal 1

# working with current game

def stateVillage(villageId, timing = 0):
    factor = timing / 3600
    ressources = currentRessources[villageId] # shouldn't we make a copy ?
    for i in range(4):
        ressources[i] = int(ressources[i] + factor * production[villageId][i])
    return villageId, ressources, production[villageId]

def state(timing = 0):
    initResAndProdForAllVillages()
    res = []
    #factor = timing / 3600
    for villageId in range(villagesLen):
        """ressources = currentRessources[villageId]
        for i in range(4):
            ressources[i] = int(ressources[i] + factor * production[villageId][i])"""
        #print(villageId, ressources, production[villageId])
        #res += [villageId, ressources, production[villageId]]
        res += stateVillage(timing, villageId)
        #print(res)
    return res

def initResAndProdForAllVillages():
    for villageId in range(villagesLen):
        initResAndProd(villageId)

#initResAndProdForAllVillages()
#state()

def nextBuildingBuiltVillage(villageId):
    driver.get(VILLAGE1SELECT(villageId))
    elems = driver.find_elements_by_class_name("buildDuration")
    elemsLen = len(elems)
    for elemsIndex in range(elemsLen): # by definition could only consider first element in queue
        elem = elems[elemsIndex]
        inner = elem.get_attribute('innerHTML')
        value = int(inner.split('value="')[1].split('"')[0])
        return value

def nextBuildingBuilt():
    next = None
    for villageId in range(villagesLen):
        #village = villages[villageId]
        value = nextBuildingBuiltVillage(villageId)
        if value is not None and (next is None or value < next):
            next = value
    return next

#print(nextBuildingBuilt())
#print()
#timing = nextBuildingBuilt()
#state(timing)

def gidFromName(buildingName, villageId):
    driver.get(VILLAGE2SELECT(villageId))
    elem = driver.find_element_by_id("village_map")
    inner = elem.get_attribute('innerHTML')
    parts = inner.split('buildingSlot a')
    partsLen = len(parts)
    for partsIndex in range(1, partsLen):
        part = parts[partsIndex].split(' teuton')[0]
        partParts = part.split()
        partPartsLen = len(partParts)
        if partPartsLen >= 3:
            print(part)

f = open("buildingsCost.txt")
line = f.readline()
f.close()
BUILDINGS_COST = eval(line)

batiments = evalFile("batiments.txt") # need ANSI encoding to work fine or should change python file read for utf8
batimentsLen = len(batiments)
for batimentsIndex in range(batimentsLen):
    batiment = batiments[batimentsIndex]
    #print(batimentsIndex + 1, batiment)
# BUILDINGS_COST[getGid("Mur de terre") - 2][4]

def getGid(buildingName):
    batimentsLen = len(batiments)
    for batimentsIndex in range(batimentsLen):
        batiment = batiments[batimentsIndex]
        if batiment == buildingName:
            return batimentsIndex + 1
    return -1

def improveBuilding(buildingName, villageId, id = -1):
    #gidFromName(buildingName, villageId)
    gid = getGid(buildingName)
    #print(gid)
    return improve(id, gid, 2, villageId)

#print("Going to sleep " + str(timing) + " seconds !")
#time.sleep(timing)
#print(improveBuilding("Académie", 2))
#print(improveBuilding("Place de rassemblement", 0)) # 8
#print(improveBuilding("Mine de fer", 2))
#print(improveBuilding("Carrière d'argile", 2, 6))
#print(improveBuilding("Mine de fer", 2, 11))

def sendRessources(villageIdDep, villageIdArr, res):
    for i in range(4):
        if currentRessources[villageIdDep][i] < res[i]:
            _, _, s = getTimeWhenEnoughRes(villageIdDep, res)
            echo("Departure village hasn't enough ressources, waiting " + str(s) + " seconds !") # should here take care of villageDep production
            time.sleep(s)
            return sendRessources(villageIdDep, villageIdArr, res)#False

    for i in range(4):
        if res[i] > 0:
            break
        if i == 3:
            i = 4
    #print(i)
    if i == 4:
        echo("Arrival village already have required ressources !")
        return None#True # used to be False
    #return

    driver.get(VILLAGE2SELECT(villageIdDep))
    driver.get(id(-1, -1, getGid("Place du marché")) + "&t=5")

    elem = driver.find_element_by_class_name("traderCount")
    inner = toAscii(elem.get_attribute('innerHTML'))
    maxTraders = int(inner.split('"merchantsAvailable">')[1].split("</span>")[0])

    for i in range(4):
        if res[i] != 0: # a bit of optimization
            elem = driver.find_element_by_name("r" + str(i + 1))
            elem.send_keys(str(res[i]))

    elem = driver.find_element_by_name("dname") # need to be after in order to have traders number refreshed
    elem.send_keys(str(villageIdArr))

    #time.sleep(1) # shouldn't be so useful

    elem = driver.find_element_by_id("merchantsNeededNumber")
    inner = elem.get_attribute('innerHTML')
    traders = int(inner)

    #echo("Need " + str(traders) + " traders, have " + str(maxTraders))
    if traders > maxTraders:
        echo("Need " + str(traders) + " traders, only have " + str(maxTraders)) # could make a force parameter which returns False without waiting
        while traders > maxTraders:
            #time.sleep(1)
            elems = driver.find_elements_by_class_name("timer")
            elemsLen = len(elems)
            if elemsLen == 0:
                echo("Doesn't have any trader \"en route\"")
                return False
            elem = elems[0]
            #inner = elem.get_attribute('innerHTML')
            timing = int(elem.get_attribute('value')) # todo: there is a bug here if need too many traders but haven't enough in general
            echo("Waiting incoming trader " + str(timing) + " seconds !") # might not be incoming but just delivery...
            time.sleep(timing)
            driver.get(VILLAGE2SELECT(villageIdDep)) # could remove both get here but likewise we couldn't use this tab manually while waiting without putting to old state
            driver.get(id(-1, -1, getGid("Place du marché")) + "&t=5")
            elem = driver.find_element_by_class_name("traderCount")
            inner = toAscii(elem.get_attribute('innerHTML'))
            maxTraders = int(inner.split('"merchantsAvailable">')[1].split("</span>")[0]) # also need to put back values...
        #return True
        # could consider reducing res because of arrival village production
        echo("Trying again")
        return sendRessources(villageIdDep, villageIdArr, res)

    elem = driver.find_element_by_id("enabledButton")
    elem.click()

    elem = driver.find_element_by_id("enabledButton")
    elem.click()

    return True

def sendRessourcesToHave(villageIdDep, villageIdArr, want):
    resNeeded = [0] * 4
    for i in range(4):
        resNeeded[i] = want[i] - currentRessources[villageIdArr][i]
        if resNeeded[i] < 0:
            resNeeded[i] = 0
    #print(resNeeded)
    #return # return None by default
    return sendRessources(villageIdDep, villageIdArr, resNeeded)

#SPEED_TRADER = 12
#SPEED_TRADER = 25.6 # let put a bit higher value - stupid me
SPEED_TRADER = 12 * 3

def timeBetween(villageId0, villageId1):
    res = 3600 * distanceVillages(villageId0, villageId1) / SPEED_TRADER
    return math.ceil(res)#res

def sendRessourcesToHaveCountingProd(villageIdDep, villageIdArr, want):
    #initResAndProdForAllVillages() # following approach make constant instead of linear complexity
    initResAndProd(villageIdDep)
    initResAndProd(villageIdArr)

    #villageDepX, villageDepY = villagesCoo[villageIdDep]
    #villageArrX, villageArrY = villagesCoo[villageIdArr]
    d = distanceVillages(villageIdDep, villageIdArr) #distance(villageDepX, villageDepY, villageArrX, villageArrY)
    factor = d / SPEED_TRADER # could use timeBetween here (warning hour fraction here !)
    for i in range(4):
        amount = int(factor * production[villageIdArr][i])
        #print(amount)
        want[i] -= amount
        if want[i] < 0:
            want[i] = 0
    return sendRessourcesToHave(villageIdDep, villageIdArr, want)

def getBuildingLevel(mid, gid, villageId): # could make it load once for all
    driver.get(VILLAGE2SELECT(villageId))
    url = id(mid, -1, gid)# + "&" + villageSelect(villageId)
    #print(url)
    driver.get(url)
    # could get url for not existing building or do like following
    elems = driver.find_elements_by_class_name("titleInHeader")
    elemsLen = len(elems)
    if elemsLen > 0:
        elem = elems[0]
        inner = elem.get_attribute('innerHTML')
        return int(inner.split('Niveau ')[1].split('</span>')[0])
    return 0

def sendRessourcesToHaveCountingProdBuilding(villageIdDep, villageIdArr, buildingName, mid = -1):
    gid = getGid(buildingName)
    #print("gid", gid)
    buildingLevel = getBuildingLevel(mid, gid, villageIdArr)
    #print("buildingLevel", buildingLevel)
    # could also directly read on the webpage ressources needed ^^ but I like having an offline approach
    ressourcesNeeded = BUILDINGS_COST[gid - 1][buildingLevel][:] # + 1 might be needed for already built buildings # used to forget [:] which was doing not obvious not working things
    #print("ressourcesNeeded", ressourcesNeeded)
    return sendRessourcesToHaveCountingProd(villageIdDep, villageIdArr, ressourcesNeeded)

def improveWithTraders(villageIdDep, villageIdArr, buildingName, mid = -1):
    sendRes = sendRessourcesToHaveCountingProdBuilding(villageIdDep, villageIdArr, buildingName, mid)
    #print("sendRes", sendRes)
    if sendRes:
        gid = getGid(buildingName)
        if villageIdDep != villageIdArr:
            d = distanceVillages(villageIdDep, villageIdArr)
            timing = int(3600 * d / SPEED_TRADER)
            echo("Waiting traders " + str(timing) + " seconds !")
            time.sleep(timing)
        improveRes = improve(mid, gid, 2, villageIdArr)
        if not improveRes:
            echo("Improve couldn't be a success")
        return [True, improveRes]
    if sendRes is None:
        gid = getGid(buildingName)
        timingConstruction = nextBuildingBuiltVillage(villageIdArr)
        echo("timingConstruction", timingConstruction, villageIdArr, gid)
        if timingConstruction is not None:
            echo("Waiting construction to finish in " + str(timingConstruction) + "seconds !")
            time.sleep(timingConstruction)
        return [False, improve(mid, gid, 2, villageIdArr)]#None
    return [False, False]

def improveAfterWithTraders(villageIdDep, villageIdArr, buildingName, mid = -1):
    timing = nextBuildingBuiltVillage(villageIdArr)
    if timing is not None:
        echo("Waiting construction to finish " + str(timing) + " seconds !")
        time.sleep(timing)
    return improveWithTraders(villageIdDep, villageIdArr, buildingName, mid)

def improveDirectlyAfterWithTraders(villageIdDep, villageIdArr, buildingName, mid = -1):
    d = distanceVillages(villageIdDep, villageIdArr)
    timingTrader = int(3600 * d / SPEED_TRADER) + 1 # + 1 seems necessary sometimes

    timingConstruction = nextBuildingBuiltVillage(villageIdArr)
    if timingConstruction is not None:
        if timingConstruction > timingTrader:
            timeToWait = timingConstruction - timingTrader
            echo("Waiting optimized time to send traders (if needed) in " + str(timeToWait) + " seconds !")
            time.sleep(timeToWait)
        if sendRessourcesToHaveCountingProdBuilding(villageIdDep, villageIdArr, buildingName, mid):
            echo("Waiting traders " + str(timingTrader) + " seconds !")
            time.sleep(timingTrader)
            gid = getGid(buildingName)
            return [True, improve(mid, gid, 2, villageIdArr)]
        else:
            return [False, False]
    else:
        return improveAfterWithTraders(villageIdDep, villageIdArr, buildingName, mid)

RAPPORTS_OTHERS = RAPPORTS + "/other"
MAX_LVL = 20 # todo: warning ! this limit depends whether or not we are considering the main village or not

# not coded to support Travian Plus (two constructions simultaneously)
def getConstructingTime(villageId):
    driver.get(VILLAGE1SELECT(villageId)) # this method in contrary to 291220 5:02 PM support also dorf2
    elems = driver.find_elements_by_class_name('buildingList')
    if len(elems) > 0:
        elem = elems[0]
        inner = elem.get_attribute('innerHTML')
        #print(inner)
        return int(inner.split('value="')[2].split('"')[0])
    return None

def lowestFarm(villageId): # copied from next function # 291220 5:02 PM
    driver.get(VILLAGE1SELECT(villageId))
    constructing = -1
    elem = driver.find_element_by_id("resourceFieldContainer")
    inner = elem.get_attribute('innerHTML')
    parts = inner.split('class="notNow level colorLayer gid')
    partsLen = len(parts)
    for partsIndex in range(1, partsLen):
        part = parts[partsIndex].split('buildingSlot')[1].split('level')[0]
        if "underConstruction" in part:
            constructing = int(part.split()[0])
            break
    loadFarmsLevelVillage(villageId)
    lvlMin = MAX_LVL
    gidMin = 0
    for gid in range(4): # gid alias farmType
        ids = RESSOURCES_FARMS[gid]
        idsLen = len(ids)
        for idsIndex in range(idsLen):
            id = ids[idsIndex]
            lvl = CURRENT_FARMS[villageId][id - 1]
            if id != constructing and lvl < lvlMin:
                lvlMin = lvl
                mid = id
                gidMin = gid
    return gidMin, lvlMin

def improveDirectlyAfterWithTradersNoLog(villageIdDep, villageIdArr, buildingName, mid = -1, level = -1, lowest = False, lowestFarmInGeneral = False):
    if villageIdDep == -1:
        villageIdDep = SUPPORT_VILLAGE # could also select the village which would produce the required ressources the fastest (if haven't already them) excepting villageIdArr
    if lowest or lowestFarmInGeneral:
        driver.get(VILLAGE1SELECT(villageIdArr))
        constructing = -1
        elem = driver.find_element_by_id("resourceFieldContainer")
        inner = elem.get_attribute('innerHTML')
        parts = inner.split('class="notNow level colorLayer gid')
        partsLen = len(parts)
        for partsIndex in range(1, partsLen):
            part = parts[partsIndex].split('buildingSlot')[1].split('level')[0]
            #print(part)
            if "underConstruction" in part:
                constructing = int(part.split()[0])
                break
        loadFarmsLevelVillage(villageIdArr)
        lvlMin = MAX_LVL # could use lowestFarm function
        if lowestFarmInGeneral: # mostly copied form following statement
            gidMin = 0 # could initialize to -1 but there is already an assignement check
            for gid in range(4): # gid alias farmType
                ids = RESSOURCES_FARMS[gid]
                idsLen = len(ids)
                for idsIndex in range(idsLen):
                    id = ids[idsIndex]
                    lvl = CURRENT_FARMS[villageIdArr][id - 1]
                    if id != constructing and lvl < lvlMin:
                        lvlMin = lvl
                        mid = id
                        gidMin = gid
            buildingName = batiments[gidMin] # might be optionnal
        else:#if lowest:
            gid = getGid(buildingName)
            ids = RESSOURCES_FARMS[gid - 1]
            idsLen = len(ids)
            for idsIndex in range(idsLen):
                id = ids[idsIndex]
                lvl = CURRENT_FARMS[villageIdArr][id - 1]
                if id != constructing and lvl < lvlMin:
                    lvlMin = lvl
                    mid = id
                    #print(lvlMin, mid)
            #level = lvlMin
        if lvlMin == MAX_LVL:
            echo("Max level reached everywhere, abort !")
            return False
    if level != -1:
        loadFarmsLevelVillage(villageIdArr)
        # could check that a farm is given (should also manage dorf2 buildings)
        gid = getGid(buildingName)
        ids = RESSOURCES_FARMS[gid - 1]
        # could check that such a level is given... - done
        idsLen = len(ids)
        for idsIndex in range(idsLen):
            id = ids[idsIndex]
            #print(id)
            if CURRENT_FARMS[villageIdArr][id - 1] == level:
                mid = id
                break
        if mid == -1:
            echo("Can't find " + buildingName + " with level " + str(level))
            return False
    #print("improving", buildingName, mid, )
    res = improveDirectlyAfterWithTraders(villageIdDep, villageIdArr, buildingName, mid)
    #print(res)
    if res[0]:
        driver.get(RAPPORTS_OTHERS + "?opt=AAALAAwADQAOAA==") # the little problem with this method is that no trading action have to be executed while watching the ad or if there are two trading operations using this system, one will read the other so no problem if specify "toggleState=0" and not "toggleState="
        elem = driver.find_element_by_id("overview")
        inner = elem.get_attribute("innerHTML")
        parts = inner.split('href="')
        partsLen = len(parts)
        for partsIndex in range(1, partsLen):
            part = parts[partsIndex].split('"')[0]
            if "toggleState=0" in part: # should be toggleState=0 in fact
                #print(part)
                url = RAPPORTS_OTHERS + part.replace("amp;", "")
                #print(url)
                driver.get(url)
                return True
        echo("Can't find an unread rapport about trading...")
        return False
    else:
        return res[1]
    return False # useless code

#sendRessources(0, 2, [500, 500, 500, 500])
#print(sendRessources(0, 1, [0, 1400, 800, 500]))
#print(sendRessourcesToHave(0, 1, [1520, 1950, 1520, 435]))
#print(sendRessourcesToHaveCountingProd(0, 1, [1520, 1950, 1520, 435]))
#print(sendRessourcesToHaveCountingProd(0, 2, [195, 250, 195, 55]))
#print(sendRessourcesToHaveCountingProd(0, 2, [195, 250, 195, 55]))
#print(sendRessourcesToHaveCountingProdBuilding(0, 2, "Silo"))
#print(improveWithMarchands(0, 2, "Silo"))
# make a version executed after construction done - done
#print(improveAfterWithMarchands(0, 2, "Silo"))
# make a version executed after construction done optimized (likewise don't wait end of construction to send marchands) - done
#print(improveDirectlyAfterWithTraders(0, 2, "Silo"))
#print(improveDirectlyAfterWithTraders(0, 1, "Champ de céréales", 2)) # "Champ de céréales" or "Ferme" love you travian guys - I could add synonym
#print(improveDirectlyAfterWithTraders(0, 2, "Dépôt"))

#echo(improveDirectlyAfterWithTraders(0, 2, "Mine de fer", 11))
#echo(improveDirectlyAfterWithTraders(0, 0, "Scierie"))

# add in improve a wait for pub to be whole watched - done

# specify level instead of mid ? - done
# read rapport - done
#echo(improveDirectlyAfterWithTradersNoLog(0, 2, "Mine de fer", 4))

stuff = {106: "Onguent", 58: "Epée courte du cavalier teuton", 145: "Bois", 146: "Argile", 147: "Fer", 148: "Céréales", 112: "Petit bandage", 114: "Cage"} # not the displayed name because they aren't regular

def isRessource(itemName):
    return itemName in ["Bois", "Argile", "Fer", "Céréales"]

#elem = driver.find_element_by_id("itemsToSale")
if False:
    driver.get(HERO)
    inventoryId = 1
    while True:
        elems = driver.find_elements_by_id("inventory_" + str(inventoryId))
        elemsLen = len(elems)
        if elemsLen == 0:
            break
        for elemsIndex in range(elemsLen):
            elem = elems[elemsIndex]
            inner = elem.get_attribute('innerHTML')
            if inner != "":
                #print("!" + inner + "!")
                #itemId = elem.get_attribute('class') # this doesn't work because we haven't selected the perfect thing (which doesn't seem easy)
                itemId = int(inner.split('class="')[1].split('"')[0].split('_')[-1])
                #print("!" + str(itemId) + "!")
                amount = int(inner.split('amount">')[1].split('</div>')[0])
                itemName = stuff[itemId]
                if isRessource(itemName):#itemName == "Bois": # could check before taking that dépôts are enoughly big
                    elem.click()
                    elems = driver.find_elements_by_class_name("buttons") # textButtonV1 green dialogButtonOk ok
                    while len(elems) == 0:
                        time.sleep(1)
                        elems = driver.find_elements_by_class_name("buttons")
                    while driver.find_element_by_class_name("displayAfterUse").get_attribute('innerHTML') == driver.find_element_by_class_name("rowBeforeUse").get_attribute('innerHTML').split('<td>')[1].split('</td>')[0]:
                        time.sleep(1)
                    elems[0].click()
                    time.sleep(1)
                #print(itemName, amount)
        inventoryId += 1
# class and amount are the only interesting fields
# could be cool to grab out the exeact name of the item (from the webpage)

def prct(x):
    return round(100 * x, 1)

def fillingDepotAndSilo(villageId):
    #driver.get(VILLAGE1SELECT(villageId))
    initResAndProd(villageId)
    fillingDepot = 0
    for i in range(3):
        fillingDepotRes = currentRessources[villageId][i] / currentDepots[villageId][0]
        if fillingDepotRes > fillingDepot:
            fillingDepot = fillingDepotRes
    fillingSilo = currentRessources[villageId][3] / currentDepots[villageId][1]
    return [[prct(fillingDepot), prct(fillingSilo)], [prct(currentRessources[villageId][i] / currentDepots[villageId][0]) for i in range(3)] + [prct(currentRessources[villageId][3] / currentDepots[villageId][1])]]

def buildLevel(villageId, gid, mid = -1): # this function might already exist but does it do EXACTLY the same thing ?
    url = VILLAGE2SELECT(villageId)
    driver.get(url)
    url = id(mid, -1, gid)
    #echo(url)
    driver.get(url)
    elem = driver.find_element_by_class_name("level")
    inner = elem.get_attribute('innerHTML').replace('Niveau ', '')
    return int(inner)

SUPPORT_VILLAGE = 0

# todo: consider investing in moulin...
# the following function works perfectly only when there is a SINGLE village and SINGLE depots !
def spendMyMoney(): # Just For Fun (2:36 AM 29/12/20) alias spendRessources (don't think here about gold or silver coins)
    # troops or farms/buildings ?
    # let say farms while "regulating" ressources or just lowest ?
    # checking that no problem doing this if with current entrepots otherwise make them grow
    # if too much do troops or just by hand sometimes ? or make a ratio ?

    # let's choose which village to work on:
    #depotMax, siloMax = 0, 0
    maxiMax = 0
    l = [fillingDepotAndSilo(villageId) for villageId in range(villagesLen)]
    #print(l)
    depots, fillings = [], [] # necessary ? - yes
    for villageId in range(villagesLen):
        depots += [l[villageId][0]]
        fillings += [l[villageId][1]]
    villageMax = -1
    villageConstructingTime = None
    for villageId in range(villagesLen): # should consider production to see which village would have its depots full first # 15 cc
        #depot, silo = fillingDepotAndSilo(villageId)
        #depot, silo = depots[villageId]
        depot, silo = depots[villageId][0], depots[villageId][1]
        maxi = max(depot, silo)
        """if depot > depotMax:
            depotMax = depot
            villageMax = villageId
        if silo > siloMax:
            siloMax = silo
            villageMax = villageId"""
        constructing = getConstructingTime(villageId) # JUST BUILD INSTEAD OF WORK ON HEAVY VILLAGE method here
        timingTrader = timeBetween(SUPPORT_VILLAGE, villageId) # maxi > maxiMax
        #print(constructing, timingTrader) # constructing < timingTrader
        if (constructing is None or (villageConstructingTime is None or constructing < villageConstructingTime)): # might need to change this if sub villages aren't at the same distance
            maxiMax = maxi
            villageMax = villageId
            villageConstructingTime = constructing if constructing is not None else 0
    echo("Going to work on village " + str(villageMax))
    workOnDepotRes = depots[villageMax][0] > depots[villageMax][1]
    #if maxiMax > 0.8:
    # let's see if will lose ressources if built farm and then associated depot (works fine for both depot types ?)
    gidMin, lvlMin = lowestFarm(villageMax)
    batimentPrincipal = buildLevel(villageMax, 15)
    #print(gidMin, lvlMin + 1, batimentPrincipal - 1)
    bPMinus1 = batimentPrincipal - 1
    #echo(str([gidMin, lvlMin + 1, bPMinus1]))
    timing = 0.75 * BUILD_TIME[gidMin][lvlMin + 1][bPMinus1]
    if workOnDepotRes:
        depotLvl = buildLevel(villageMax, 10)
        #time.sleep(5)
        depot = 0.75 * BUILD_TIME[9][depotLvl + 1][bPMinus1]
    else:
        siloLvl = buildLevel(villageMax, 11)
        #time.sleep(5)
        #echo(str([siloLvl, bPMinus1]))
        depot = 0.75 * BUILD_TIME[10][siloLvl + 1][bPMinus1]
    #state()
    #print(state())
    #print(state(timing))
    inv = 1 / 0.75 # 1.333...
    #print(workOnDepotRes, timing * inv, depot * inv)
    #print(stateVillage(villageMax))

    future = stateVillage(villageMax, timing + depot) # could remove villageId from return of stateVillage...
    #print(workOnDepotRes, future, depots[villageMax])
    overflow = False
    if workOnDepotRes:
        for i in range(3):
            if future[1][i] > currentDepots[villageMax][0]:#depots[villageMax][0]:
                overflow = True
                break
    else:
        if future[1][3] > currentDepots[villageMax][1]:#depots[villageMax][1]:
            overflow = True
    if overflow:
        echo("Going to improve " + ("depot" if workOnDepotRes else "silo") + " !")
        echo(improveDirectlyAfterWithTradersNoLog(SUPPORT_VILLAGE, villageMax, "Dépôt" if workOnDepotRes else "Silo"))
    else:
        farmType = 0
        villageConsidered = SUPPORT_VILLAGE#villageMax
        lowest = fillings[villageConsidered][0] # COULD CONSIDER SUPPORT_VILLAGE instead of sub village ... or the global factor on all villages
        print(fillings)
        for i in range(1, 4):
           if fillings[villageConsidered][i] < lowest:
               lowest =  fillings[villageConsidered][i]
               farmType = i
        batiment = batiments[farmType]
        echo("Going to improve farm " + batiment + " !")
        echo(improveDirectlyAfterWithTradersNoLog(SUPPORT_VILLAGE, villageMax, batiment))
    #print(villageMax, stateVillage(villageMax, timing + depot)) # TODO: should also consider production increase
    # is it going to be debording ? if so build associated depot otherwise the farm - done

    # let's focus for the moment on buildings/farms:
while True:
    spendMyMoney()

# todo: could make a sleep which can be broken every n seconds

##

#echo(improveDirectlyAfterWithTradersNoLog(0, 2, "Mine de fer", -1, 4))
#echo("hey") # 2 s of verification/process here

#echo(improveDirectlyAfterWithTradersNoLog(0, 2, "Carrière d'argile", -1, 4))
# make a parameter to improve lowest level of given buildingName - done

## 0

echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "Bûcheron", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "Carrière d'argile", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "Mine de fer", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "Champ de céréales", -1, -1, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "", -1, -1, False, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 0, "Usine de poteries"))

## 1

echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Bûcheron", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Carrière d'argile", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Mine de fer", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Champ de céréales", -1, -1, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "", -1, -1, False, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Place de rassemblement"))
echo(improveDirectlyAfterWithTradersNoLog(-1, 1, "Moulin"))

## 2

# to test (with same top left constructing) - done
echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Bûcheron", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Carrière d'argile", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Mine de fer", -1, -1, True))
echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Champ de céréales", -1, -1, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "", -1, -1, False, True))

echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Place de rassemblement"))
echo(improveDirectlyAfterWithTradersNoLog(-1, 2, "Mur de terre"))

##

# tool to improve lowest farm - done
# todo: multiple at the same time
# add a wait if villageDep hasn't enough ressources ? - done
# todo: also manage building and not only improving
# traders are coming back ? - done
# could (I said could) use directly ajax etc instead of clicking on buttons etc it would be faster
# maybe we should parallelize things like one tab/window for attack/defense one for building... (might desync ? si chacun essaye de tirer la couette de son côté)

## close

driver.close()
