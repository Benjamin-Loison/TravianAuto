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
    print(now + " | " + s)

VILLAGE1, VILLAGE2 = php("dorf1"), php("dorf2")
def villageSelect(villageId):
    return "newdid=" + str(villages[villageId])

def VILLAGE1SELECT(villageId):
    return VILLAGE1 + "?" + villageSelect(villageId)

def VILLAGES2ELECT(villageId):
    return VILLAGE2 + "?" + villageSelect(villageId)
MAP = php("karte")

def mapXY(x, y):
    return MAP + "?x=" + str(x) + "&y=" + str(y)

RASSEMBLEMENT = building(16)
SITUATION = RASSEMBLEMENT + "&tt=1"
ENVOI_DE_TROUPES = RASSEMBLEMENT + "&tt=2"
CARRIERE_D_ARGILE = building(2)
CARRIERE_D_ARGILE_6 = CARRIERE_D_ARGILE + "&id=6"
VILLAGE_BUILD_29 = id(29, 1)
ADVENTURES = page("hero/adventures")

pillages = {}
pillages["fiodor"] = [71, -26]

driver = webdriver.Firefox()

driver.get(VILLAGE1)
#time.sleep(2)
elem = driver.find_element_by_name("name")
elem.send_keys(playing)
elem = driver.find_element_by_name("password")
elem.send_keys(crendentials[playing])
elem.send_keys(Keys.RETURN)

GID_WOOD, GID_BRICK, GID_IRON, GID_CEREAL = 1, 2, 3, 4

WOODS, BRICKS, IRONS, CEREALS = [1, 3, 14, 17], [5, 6, 16, 18], [4, 7, 10, 11], [2, 8, 9, 12, 13, 15]
farms = {}#{1: GID_WOOD, 3: GID_WOOD, 14: GID_WOOD, 17: GID_WOOD,
#2: GID_CEREAL, 8}
for ELEMS, GID in zip([WOODS, BRICKS, IRONS, CEREALS], [GID_WOOD, GID_BRICK, GID_IRON, GID_CEREAL]):
    for elem in ELEMS:
        farms[elem] = GID

def toAscii(s):
    return s.replace('(', '').replace(')', '').replace('\u202c', '').replace('\u202d', '').replace("\n", "").replace(" ", "").replace('−', '-').replace('\t', '')

natureNames = ["rat", "araignée", "serpent", "chauve-souris", "sanglier", "loup", "ours", "crocodile", "tigre", "éléphant"]
natureDef = [[25, 20], [35, 40], [40, 60], [66, 50], [70, 33], [80, 70], [140, 200], [380, 240], [170, 250], [440, 520]]
natureDefAverage = []
for natureD in natureDef:
    #cavalerie, infanterie = natureD
    natureDefAverage += [sum(natureD) / len(natureD)]

# 1-1-1-15 finder ? - done

travianAutoPath = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Projects\\TravianAuto\\"
os.chdir(travianAutoPath)