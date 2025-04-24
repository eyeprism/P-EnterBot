import multiprocessing
import pathlib
import time
import csv
import os

import pyautogui
import keyboard


pyautogui.FAILSAFE = False

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

IMAGE_DIR = pathlib.Path('Images/')

#default value for teams
#program uses csv file for teams after csv file is created
teams = [
    [1, "Charge","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya", "Sinclair", "Outis", "Gregor"],
    [2, "Sinking","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya", "Sinclair", "Outis", "Gregor"],
    [3, "Bleed","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya",  "Sinclair", "Outis", "Gregor"],
    [4, "Burn","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya", "Sinclair", "Outis", "Gregor"],
    [5, "Rupture","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya", "Sinclair", "Outis", "Gregor"],
    [6, "Tremor","YiSang", "Faust", "Don", "Ryoshu", "Meursault", "HongLu", "Heathcliff", "Ishmael", "Rodya", "Sinclair", "Outis", "Gregor"]
]

SINNER_COORDINATES = {
    "yisang": (435, 339),
    "faust": (637, 331),
    "don": (838, 340),
    "ryoshu": (1026, 343),
    "meursault": (1238, 345),
    "honglu": (1429, 352),
    "heathcliff": (436, 647),
    "ishmael": (634, 640),
    "rodya": (842, 636),
    "sinclair": (1041, 628),
    "outis": (1232, 639),
    "gregor": (1432, 646),
}

def locateOnScreenBool(image, confidence = 0.999, grayscale = True, region = (0,0,1920,1080)):
    try:
        pyautogui.locateOnScreen(image, confidence = confidence, grayscale = grayscale, region = region)
        return True
    except:
        return False

def setScreenSize():
    global width, height
    width,height = pyautogui.size()
    if (width, height) != (1920, 1080):
        print("Wrong Resolution Buster")
        quit()

def neutralizeMousePos():
    pyautogui.moveTo(width/2,0)

def findState():
    #Title screen
    if locateOnScreenBool("Images/ClearAllCaches.png", confidence = 0.8, grayscale = True, region = (285, 950, 250, 100)):
        return 0
    if locateOnScreenBool("Images/Drive.png", confidence = 0.75, grayscale = True, region = (1236,907,150,150)): #Drive button visable
        if locateOnScreenBool("Images/MD5Button.png", confidence = 0.8, grayscale = True, region = (520,351,300,250)): #Mirror dungeon button visable
            return 2
        return 1
    if locateOnScreenBool("Images/MD5StartButton.png", confidence = 0.6, grayscale = True, region = (715,255,550,650)):
        return 3
    if locateOnScreenBool("Images/EnterMD5.png", confidence = 0.8, grayscale = True, region = (960,690,400,100)):
        return 4
    if locateOnScreenBool("Images/RestBonus.png", confidence = 0.75, grayscale = True, region = (1620,784,150,100)):
        return 5
    if locateOnScreenBool("Images/DungeonProgress.png", confidence = 0.75, grayscale = True, region = (812,325,300,100)):
        return 6
    if locateOnScreenBool("Images/Starlight_Guidance.png", confidence = 0.75, grayscale = True, region = (828,579,350,200)):
        return 7
    if locateOnScreenBool("Images/Will_You_Buff.png", confidence = 0.75, grayscale = True, region = (760,293,450,100)):
        return 8
    if locateOnScreenBool("Images/Starting_Gift.png",confidence = 0.8, grayscale = True, region = (1100,150,600,300)):
        return 9
    if locateOnScreenBool("Images/EGO_GIFT_GET.png",confidence = 0.8, grayscale = True, region = (817,249,350,100)):
        return 10
    if locateOnScreenBool("Images/Theme_Pack.png",confidence = 0.8, grayscale = True, region = (967,150,250,100)):
        return 11
    if locateOnScreenBool("Images/NodeSelect.png",confidence = 0.9, grayscale = True, region = (1802,115,100,100)):
        return 12
    if locateOnScreenBool("Images/Event_Skip.png", confidence = 0.8, grayscale = True, region = (849,443,150,100)):
        return 13
    if locateOnScreenBool("Images/Team_TotalParticipants.png", confidence = 0.8, grayscale = True, region = (1595,750,150,100)):
        return 14
    if locateOnScreenBool("Images/Battle_Winrate.png", confidence = 0.8, grayscale = True, region = (800,750,1120,200)):
        return 15
    if locateOnScreenBool("Images/Shop_Refresh.png", confidence = 0.8, grayscale = True, region = (1385,147,250,100)):
        return 16
    if locateOnScreenBool("Images/Select_Encounter_Reward.png", confidence = 0.8, grayscale = True, region = (383, 148,850,150)):
        return 17
    if locateOnScreenBool("Images/RefuseGift.png", confidence = 0.8, grayscale = True, region = (1285,816,300,150)):
        return 18
    if locateOnScreenBool("Images/End_Passlvlup.png", confidence = 0.8, grayscale = True, region = (818,347,350,100)):
        return 19
    if locateOnScreenBool("Images/End_Victory.png", confidence = 0.8, grayscale = True, region = (1375,150,500,500)):
        return 20
    if locateOnScreenBool("Images/End_ClaimTheRewards.png", confidence = 0.7, grayscale = True, region = (750,450,450,200)):
        return 21
    if locateOnScreenBool("Images/End_ClaimTheRewards1.png", confidence = 0.7, grayscale = True, region = (750,450,450,200)):
        return 22
    if locateOnScreenBool("Images/End_ExplorationReward.png", confidence = 0.8, grayscale = True, region = (725,126,400,100)):
        return 23
    if locateOnScreenBool("Images/End_ExplorationComplete.png", confidence = 0.8, grayscale = True, region = (179,112,300,200)):
        return 24
    if locateOnScreenBool("Images/End_Defeat.png", confidence = 0.8, grayscale = True, region = (1475,192,300,150)):
        return 25
    return -1 #unknown state/tansitionary state

def getToMirrorDungeon():
    while(True):
        time.sleep(0.1)
        state = findState()
        print(state)
        match state:
            case 0:
                pyautogui.click(x = width/2, y = height/2)
            case 1:
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/Drive.png", confidence = 0.75, grayscale = True, region = (1236,907,150,150)))
                except:
                    pass
            case 2:
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/MD5Button.png", confidence = 0.8, grayscale = True, region = (520,351,300,250)))
                except:
                    pass
            case 3:
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/MD5StartButton.png", confidence = 0.2, grayscale = True, region = (715,255,550,650)))
                except:
                    pass
            case 4:
                try:
                    neutralizeMousePos()
                    pyautogui.click(pyautogui.locateOnScreen("Images/EnterMD5.png", confidence = 0.8, grayscale = True, region = (950,680,450,150)))
                except:
                    pass
            case 6:
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/ResumeMD5.png", confidence = 0.8, grayscale = True, region = (781,566,400,100)))
                except:
                    pass
            case -1:
                pass
            case _:
                return



def getRestBonus() -> int:
    restBonusRegion = (1750,780,60,60)
    nums = set()
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_0.png", region=restBonusRegion, confidence = 0.95)
        for i in temp:
            nums.add((i.left, 0))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_1.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 1))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_2.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 2))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_3.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 3))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_4.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 4))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_5.png", region=restBonusRegion, confidence = 0.925)
        for i in temp:
            nums.add((i.left, 5))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_6.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 6))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_7.png", region=restBonusRegion, confidence = 0.925, graycsale = True)
        for i in temp:
            nums.add((i.left, 7))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_8.png", region=restBonusRegion, confidence = 0.95)
        for i in temp:
            nums.add((i.left, 8))
    except:
        pass
    try:
        temp = pyautogui.locateAllOnScreen("Images/RestBonus_9.png", region=restBonusRegion, confidence = 0.9)
        for i in temp:
            nums.add((i.left, 9))
    except:
        pass
    digitList = sorted(nums, reverse=True)
    returnVal = 0
    counter = 0
    for i in digitList:
        returnVal += i[1] * (pow(10,counter))
        counter += 1
    return returnVal

def scrollTo(dest, cur) -> int:
    diff = cur - dest
    baseDrag = 86
    for i in range(abs(diff)):
        pyautogui.mouseDown()
        pyautogui.moveRel(0,baseDrag* diff/abs(diff),duration = 0.3, tween = pyautogui.easeOutQuad)
        time.sleep(0.3)
        pyautogui.mouseUp()
        pyautogui.moveRel(0,-baseDrag*diff/abs(diff))
    return dest

def selectTeam():
    global curTeam
    pyautogui.moveTo(pyautogui.locateOnScreen("Images/Teams.png", confidence = 0.8, grayscale = True, region = (72,527,200,100)))
    pyautogui.moveRel(0,50)
    for i in range(30):
        pyautogui.scroll(clicks = 100)
    curRow = 1
    maxBonus = 0
    maxTeamRow = 1
    for i in teams:
        curRow = scrollTo(int(i[0]),curRow)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.1)
        RB = getRestBonus()
        print("Row:", curRow, " Rest Bonus:", RB)
        if RB > maxBonus:
            maxBonus = RB
            maxTeamRow = int(i[0])
            curTeam = i
    curRow = scrollTo(maxTeamRow,curRow)
    time.sleep(0.1)
    pyautogui.click()
    while(True):
        try:
            pyautogui.click(pyautogui.locateOnScreen("Images/ConfirmTeam.png", confidence = 0.8))
            break
        except:
            pass
    time.sleep(1)



def teamConfigRoutine():
    global teams
    global curTeam
    if not os.path.exists("Config"):
        os.makedirs("Config")
        makeConfig()
    elif not os.path.exists("Config/TeamConfig.csv"):
        makeConfig()
    with open('Config/TeamConfig.csv', 'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        teams = list()
        for row in csv_reader:
            if i > 0:
                teams.append(row)
            i += 1
        curTeam = teams[0]


def makeConfig():
    with open("Config/TeamConfig.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        header = ["TeamRow","Type","Sinner1", "Sinner2", "Sinner3", "Sinner4", "Sinner5", "Sinner6", "Sinner7", "Sinner8", "Sinner9", "Sinner10", "Sinner11", "Sinner12"]
        csv_writer.writerow(header)
        csv_writer.writerows(teams)

def selectBuffs():
    pyautogui.click(963,727)
    pyautogui.click(682,725)
    pyautogui.click(1250,280)
    pyautogui.click(400,400)
    pyautogui.click(700,400)
    pyautogui.click(1706,991)

def selectStartingGifts():
    giftType = curTeam[1].lower()
    match giftType:
        case "charge":
            pyautogui.click(758,667)
        case "sinking":
            pyautogui.click(307,680)
        case "poise":
            pyautogui.click(522,669)
        case "rupture":
            pyautogui.click(975,359)
        case "tremor":
            pyautogui.click(748,362)
        case "bleed":
            pyautogui.click(520,360)
        case "burn":
            pyautogui.click(312,365)
        case "slash":
            pyautogui.click(980,685)
        case "blunt":
            pyautogui.click(533,844)
        case "pierce":
            pyautogui.click(313,846)
    time.sleep(0.1)
    #select gifts from top to bottom
    pyautogui.click(1463,392)
    pyautogui.click(1463,550)
    pyautogui.click(1463,713)
    #end selection
    pyautogui.click(1620,870)


#main
def mainFunc():
    curState: int = -1
    runNum: str = pyautogui.prompt(text = "Enter number of MD runs", title = "StartMenu", default = 1)

    if not runNum.isdigit():
        print("Number of runs must be integer")
        quit()

    runNum = int(runNum)

    time.sleep(0.1)
    teamConfigRoutine()
    setScreenSize()
    while runNum > 0: #Main loop
        neutralizeMousePos()
        if curState == -1:
            getToMirrorDungeon()
        time.sleep(0.1)
        curState = findState()
        print(curState)
        match curState:
            case 5: #Team Selection
                if locateOnScreenBool("Images/Teams.png",confidence = 0.8, grayscale = True, region = (72,527,200,100)):
                    selectTeam()
            case 7:#MD5 buff selection
                if locateOnScreenBool("Images/Starlight_Guidance.png",confidence = 0.75, grayscale = True, region = (828,579,350,200)):
                    selectBuffs()
            case 8:#End buff selection
                if locateOnScreenBool("Images/Will_You_Buff.png",confidence = 0.8, grayscale = True, region = (760,293,450,100)):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/ConfirmBuff.png",confidence = 0.8))
                    except:
                        pass
            case 9:#Starting Gift Selection
                if locateOnScreenBool("Images/Starting_Gift.png",confidence = 0.8, grayscale = True, region = (1100,150,600,300)):
                    selectStartingGifts()
            case 10:
                if locateOnScreenBool("Images/EGO_GIFT_GET.png", confidence = 0.8, grayscale = True, region = (817,249,350,100)):
                    pyautogui.click(pyautogui.locateOnScreen("Images/EGOGift_Confirm.png",confidence = 0.8))
            case 11:#Pack Selection
                if locateOnScreenBool("Images/Pack_Hard.png", confidence = 0.8):
                    pyautogui.click(1363, 100)
                try:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Images/Pack_Hanger.png", confidence = 0.8))
                    pyautogui.dragRel(0,500, 1)
                except:
                    pass
            case 12: #Node Selection
                if locateOnScreenBool("Images/Clock_Face.png", confidence = 0.9):
                    time.sleep(0.5)
                    located = False
                    try:
                        x,y = pyautogui.center(pyautogui.locateOnScreen("Images/Clock_Face.png", confidence = 0.9))
                        pyautogui.moveTo(x,y)
                        time.sleep(0.1)
                        x += 330
                        y -= 280
                        pyautogui.click(x,y)
                        time.sleep(0.2)
                        located = True
                    except:
                        pass
                failCounter = 0
                if located:
                    while(not locateOnScreenBool("Images/Enter_Node.png", confidence = 0.9)):
                        y += 300
                        pyautogui.click(x,y)
                        time.sleep(0.25)
                        failCounter += 1
                        if (failCounter > 3):
                            break
                    time.sleep(0.35)
                    pyautogui.click(1704,810)
            case 13:#Event
                if locateOnScreenBool("Images/Event_Choices.png", confidence = 0.8):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Event_EGOGIFT.png", confidence = 0.7))
                    except:
                        pyautogui.click(1366, 350)
                        pyautogui.click(1366, 600)
                        pyautogui.click(1366, 750)
                if locateOnScreenBool("Images/Event_Predicted.png", confidence = 0.8):
                    if locateOnScreenBool("Images/Event_VeryHigh.png", confidence = 0.7):
                        try:
                            pyautogui.click(pyautogui.locateOnScreen("Images/Event_VeryHigh.png", confidence = 0.7))
                        except:
                            pass
                    elif locateOnScreenBool("Images/Event_High.png", confidence = 0.7):
                        try:
                            pyautogui.click(pyautogui.locateOnScreen("Images/Event_High.png", confidence = 0.7))
                        except:
                            pass
                    elif locateOnScreenBool("Images/Event_Normal.png", confidence = 0.7):
                        try:
                            pyautogui.click(pyautogui.locateOnScreen("Images/Event_Normal.png", confidence = 0.7))
                        except:
                            pass
                    elif locateOnScreenBool("Images/Event_Low.png", confidence = 0.7):
                        try:
                            pyautogui.click(pyautogui.locateOnScreen("Images/Event_Low.png", confidence = 0.7))
                        except:
                            pass
                    elif locateOnScreenBool("Images/Event_VeryLow.png", confidence = 0.7):
                        try:
                            pyautogui.click(pyautogui.locateOnScreen("Images/Event_VeryLow.png", confidence = 0.7))
                        except:
                            pass
                if locateOnScreenBool("Images/Event_Commence.png", confidence = 0.8):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Event_Commence.png", confidence = 0.8))
                    except:
                        pyautogui.click(1707, 950)
                elif locateOnScreenBool("Images/Event_Continue.png", confidence = 0.8):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Event_Continue.png", confidence = 0.8))
                    except:
                        pyautogui.click(1707, 950)
                elif locateOnScreenBool("Images/Event_Proceed.png", confidence = 0.8):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Event_Proceed.png", confidence = 0.8))
                    except:
                        pyautogui.click(1707, 950)
                elif locateOnScreenBool("Images/Event_CommenceBattle.png", confidence = 0.8):
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Event_CommenceBattle.png", confidence = 0.8))
                    except:
                        pyautogui.click(1707, 950)
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/Event_Skip.png",confidence = 0.8, grayscale = True, region = (849,443,150,100)))
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()
                except:
                    pass
            case 14:#Pre fight sinner selection
                if locateOnScreenBool("Images/Team_ClearSelection.png", confidence = 0.925):
                    pyautogui.click(1715, 720)
                    time.sleep(0.5)
                    pyautogui.click(1145, 740)
                    time.sleep(0.5)
                for i in range(12):
                    pyautogui.click(SINNER_COORDINATES[curTeam[i+2].lower()])
                time.sleep(0.25)
                pyautogui.click(1720,880)
                time.sleep(0.5)
            case 15:#OMG P-ENTER!!!
                pyautogui.click(width/2,height/6)
                time.sleep(0.05)
                pyautogui.press('p')
                time.sleep(0.05)
                pyautogui.press('enter')
            case 16:#Shop
                
                try:
                    shopItems = pyautogui.locateAllOnScreen("Images/Shop_Item.png",confidence = 0.935, grayscale = True, region = (1051,325,850,700))
                    for i in shopItems:
                        pyautogui.click(i)
                        time.sleep(0.75)
                        pyautogui.click(1120,712)
                        time.sleep(0.75)
                        pyautogui.click(945,800)
                        time.sleep(0.5)
                    pass
                except:
                    pass
                try:
                    shopItems2 = pyautogui.locateAllOnScreen("Images/Shop_Item.png",confidence = 0.935, grayscale = True, region = (821,563,1150,500))
                    for i in shopItems2:
                        pyautogui.click(i)
                        time.sleep(0.75)
                        pyautogui.click(1120,712)
                        time.sleep(0.75)
                        pyautogui.click(945,800)
                        time.sleep(0.5)
                except:
                    pass
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/Shop_Leave.png", confidence = 0.8))
                    time.sleep(0.5)
                    pyautogui.click(1171,743)
                except:
                    pass
            case 17:
                try:
                    pyautogui.click(pyautogui.locateOnScreen("Images/Reward_EGOGIFT.png", confidence = 0.8))
                    time.sleep(0.5)
                except:
                    try:
                        pyautogui.click(pyautogui.locateOnScreen("Images/Reward_Cost.png", confidence = 0.8))
                        time.sleep(0.5)
                    except:
                        pass
                pyautogui.click(1200, 800)
            case 18:
                if locateOnScreenBool("Images/AcquireEGOGIFT.png", confidence = 0.8):
                    try:
                        for image in (pyautogui.locateAllOnScreen("Images/AcquireEGOGIFT.png", confidence = 0.95)):
                            pyautogui.click(image)
                            time.sleep(0.2)
                    except:
                        pass
                else:
                    try:
                        for image in (pyautogui.locateAllOnScreen("Images/Plus1.png", confidence = 0.95)):
                            pyautogui.click(image)
                            time.sleep(0.2)
                    except:
                        pass
                pyautogui.click(1705, 870)
            case 19:
                pyautogui.click(963, 700)
                runNum -= 1
                print("Runs left to do:",runNum)
            case 20:
                pyautogui.click(1671, 839)
            case 21:
                pyautogui.click(1150, 750)
            case 22:
                pyautogui.click(1150, 750)
            case 23:
                pyautogui.click(1330, 810)
            case 24:
                pyautogui.click(1700, 900)
            case 25: #Defeat failsafe
                while (True):
                    if locateOnScreenBool("Images/End_Defeat.png", confidence = 0.8, grayscale = True, region = (1475,192,300,150)):
                        pyautogui.click(1673, 840)
                    if locateOnScreenBool("Images/End_NoRewards.png", confidence = 0.8):
                        time.sleep(1)
                        pyautogui.click(1153, 740)
                        break
                    elif locateOnScreenBool("Images/End_ExplorationReward.png", confidence = 0.8):
                        pyautogui.click(587, 814)
                    elif locateOnScreenBool("Images/End_ExplorationComplete.png", confidence = 0.8):
                        pyautogui.click(1700, 900)
                    time.sleep(0.1)
        time.sleep(0.1)



if __name__ == '__main__':
    multiprocessing.freeze_support()
    process = multiprocessing.Process(target=mainFunc)#multiprocess with main function so failsafe key can be detected whenever
    process.start()
    while process.is_alive():
        time.sleep(0.1)
        if keyboard.is_pressed('q'): #failsafe
            process.terminate()
            break
