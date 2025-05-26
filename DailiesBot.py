import pyautogui, cv2, os, time, mss, keyboard,csv,numpy, multiprocessing
from PIL import Image

pyautogui.FAILSAFE = False

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

EXP_team = ['don', 'yisang','ishmael','heathcliff','rodya','gregor']

sinnerCoordinates = {
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

def setScreenSize():
    global width, height
    width,height = pyautogui.size()
    if (width, height) != (1920, 1080):
        print("Wrong Resolution Buster")
        quit()

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
    if locateOnScreenBool("Images/ClearAllCaches.png", confidence = 0.8, grayscale = True, region = (285, 950, 250, 100)):
        return 0
    if locateOnScreenBool("Images/Drive.png", confidence = 0.75, grayscale = True, region = (1236,907,150,150)): #Drive button visable
        if locateOnScreenBool("Images/MD5Button.png", confidence = 0.8, grayscale = True, region = (520,351,300,250)): #Mirror dungeon button visable
            return 2
        return 1
    if locateOnScreenBool("Images/Enter_EXPLux.png", confidence = 0.8, grayscale = True, region = (1530,699,265,44)): #1662, 711 exp lux visible
        return 3    
    if locateOnScreenBool("Images/Team_ClearSelection.png", confidence = 0.8, grayscale = False, region = (1550,650,300,100)):#1606,697
        return 4
    if locateOnScreenBool("Images/Battle_Winrate.png", confidence = 0.8, grayscale = True, region = (800,750,1120,200)):#1515 765, 1815 900
        return 5
    if locateOnScreenBool("Images/End_Victory.png", confidence = 0.8, grayscale = True, region = (1375,150,500,500)):#you win
        return 6
    if locateOnScreenBool("Images/Battle_Skill.png", confidence = 0.8, grayscale = True, region = (1172,371,1162,58)):
        return 7
    if locateOnScreenBool("Images/Enkephalin_CanAssemble.png", confidence = 0.8, grayscale = True, region = (650, 710, 600, 60)):
        return 8
    if locateOnScreenBool("Images/Luxcavation_DailyBonuses.png", confidence = 0.8, grayscale = True, region = (720, 40, 180, 40)):
        return 9
    if locateOnScreenBool("Images/End_Defeat.png", confidence = 0.8, grayscale = True, region = (1475,192,300,150)):
        return 10
    if locateOnScreenBool("Images/Enkephalin_DailyCount.png", confidence = 0.8, grayscale = True, region = (990, 410, 250, 45)):
        return 11
    if locateOnScreenBool("Images/Enkephalin_Insufficient.png", confidence = 0.8, grayscale = True, region = (800, 710, 300, 60)):
        return 12
    

    #720, 40
    return -1
    

def doEXPLux():
    done = False
    while not done:
        time.sleep(0.5)
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
                pyautogui.click(666,250)
            case 3:
                pyautogui.click(1662, 711)
                neutralizeMousePos()
            case 4:
                pyautogui.click(1715, 720)
                time.sleep(1)#700, 400, 500, 200
                if locateOnScreenBool("Images/Team_ResetDeploymentOrder.png", confidence = 0.75, grayscale = True, region = (700, 400, 500, 200)):
                    pyautogui.click(1145, 740)
                    time.sleep(1)
                for i in range(6):
                    pyautogui.click(sinnerCoordinates[EXP_team[i].lower()])
                    time.sleep(0.2)
                time.sleep(.5)
                pyautogui.click(1720,880)
                time.sleep(5)
            case 5:#OMG P-ENTER!!!
                pyautogui.click(width/2,height/6)
                time.sleep(0.05)
                pyautogui.press('p')
                time.sleep(0.05)
                pyautogui.press('enter')
            case 6:
                time.sleep(0.5)
                pyautogui.click(1660,840)
                done = True
            case 7:
                time.sleep(0.5)
                pyautogui.click(100, 100)
            case 10:
                time.sleep(0.5)
                pyautogui.click(1660,840)
            
def doThreadLux(skips):
    while skips > 0:
        time.sleep(0.5)
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
                pyautogui.click(666,250)
            case 3:
                pyautogui.click(200, 500)
            case 5:#OMG P-ENTER!!!
                pyautogui.click(width/2,height/6)
                time.sleep(0.05)
                pyautogui.press('p')
                time.sleep(0.05)
                pyautogui.press('enter')
            case 6:
                time.sleep(0.5)
                pyautogui.click(1660,840)
                skips -= 1
            case 7:
                pyautogui.click(100, 100)
            case 9:
                pyautogui.click(555, 770)
                time.sleep(0.5)
                pyautogui.click(935, 720)
                time.sleep(0.5)
                pyautogui.click(1140, 730)
                time.sleep(1)

def convertModules(refills):
    assembled = False
    while refills > 0 and assembled == False:
        time.sleep(0.5)
        state = findState()
        print(state)
        match state:
            case 0:
                pyautogui.click(x = width/2, y = height/2)
            case 1:
                pyautogui.click(570, 1000)
                time.sleep(2)
                pyautogui.click(950, 340)#use lunacy tab
                time.sleep(0.5)
            case 8:#convert modules

                #pyautogui.click(950, 340)#use lunacy tab
                #time.sleep(0.5)
                #pyautogui.click(1132, 800)#confirm
                #time.sleep(0.5)
                #pyautogui.click(750, 340)#modules tab
                #time.sleep(0.5)
                pyautogui.click(1200, 500)#right arrow
                time.sleep(0.5)
                pyautogui.click(1132, 800)#confirm
                time.sleep(0.5)
                #pyautogui.click(770, 800)#cancel
                #refills -= 1
            case 11:
                if refills > 0:
                    time.sleep(2)
                    pyautogui.click(1132, 800)#confirm
                    refills -= 1
                else:
                    time.sleep(2)
                    pyautogui.click(750, 340)#modules tab
                    time.sleep(0.5)
            case 12:
                pyautogui.click(770, 800)#cancel
                assembled = True
                


def mainFunc():
    setScreenSize()
    choice = pyautogui.prompt(text = "(1) exp lux; (2) thread lux; (3) both", title = "StartMenu", default = 1)
    try:
        choice = int(choice)
    except:
        print("Choice must be integer")
        quit()
    if choice == 2 or choice == 3:
        numThread = pyautogui.prompt(text = "how many thread skips?", title = "StartMenu", default = 1)
        try:
            numThread = int(numThread)
        except:
            print("num must be integer")
            quit()
    #refills = pyautogui.prompt(text = "how many lunacy enkephalin refills?", title = "StartMenu", default = 1)
    #try:
    #    refills = int(refills)
    #except:
    #    print("Num refills must be integer")
    #    quit()
    #convertModules(refills)
    if choice == 1 or choice == 3:
        doEXPLux()
    if choice == 2 or choice == 3:
        doThreadLux(numThread)
    

if __name__ == '__main__':
    multiprocessing.freeze_support()
    process = multiprocessing.Process(target=mainFunc)#multiprocess with main function so failsafe key can be detected whenever
    process.start()
    while process.is_alive(): 
        time.sleep(0.1)
        if keyboard.is_pressed('q'): #failsafe
            process.terminate()
            break
