import os

os.chdir("C:\\Users\\Benjamin\\Desktop\\BensFolder\\DEV\\Python\\Projects\\TravianAuto\\")

f = open("clickBuildingResNeeded.txt")
lines = f.readlines()
f.close()

linesLen = len(lines)
print('[', end = '')
for linesIndex in range(linesLen):
    line = lines[linesIndex]
    #print(line)
    lineParts = line.split()
    #print(lineParts)
    print('[', end = '')
    for i in range(1, 5):
        print(lineParts[i], end = '')
        if i != 4:
            print(', ', end = '')
    print(']', end = '')
    if linesIndex != linesLen - 1:
        print(', ', end = '')
print(']', end = '')