import pathlib
import logging
import time
import csv
import os

from dataclasses import dataclass
from typing import Self

import pyautogui

logging.basicConfig(format='%(levelname)s:%(funcName)s - %(message)s', level=logging.DEBUG)

IMAGE_DIR = pathlib.Path('Images/')

@dataclass
class GameElement:
    id: int
    image: str
    region: tuple[int, int, int, int] | None = None
    confidence: float = 0.8
    grayscale: bool = True

    def __str__(self) -> str:
        return f'{self.id=} {self.image=} {self.region=} {self.confidence=} {self.grayscale=}'

REST_BONUS_REGION = (1750,780,60,60)

GAME_ELEMENTS = {
    "ClearAllCaches" : GameElement(0, "ClearAllCaches.png", (285, 950, 250, 100)),
    "Drive" : GameElement(1, "Drive.png", (1236, 907, 150, 150), 0.75),
    "MD5Button" : GameElement(2, "MD5Button.png", (520,351,300,250)),
    "MD5StartButton" : GameElement(3, "MD5StartButton.png", (715,255,550,650), 0.6),
    "EnterMD5" : GameElement(4, "EnterMD5.png", (960,690,400,100)),
    "RestBonus" : GameElement(5, "RestBonus.png", (1620,784,150,100), 0.75),
    "DungeonProgress" : GameElement(6, "DungeonProgress.png", (812,325,300,100), 0.75),
    "Starlight_Guidance" : GameElement(7, "Starlight_Guidance.png", (828,579,350,200), 0.75),
    "Will_You_Buff" : GameElement(8, "Will_You_Buff.png", (760,293,450,100), 0.75),
    "Starting_Gift" : GameElement(9, "Starting_Gift.png", (1100,150,600,300)),
    "EGO_GIFT_GET" : GameElement(10, "EGO_GIFT_GET.png", (817,249,350,100)),
    "Theme_pack" : GameElement(11, "Theme_pack.png", (967,150,250,100)),
    "NodeSelect" : GameElement(12, "NodeSelect.png", (1802,115,100,100), 0.9),
    "Event_Skip" : GameElement(13, "Event_Skip.png"),
    "Team_Total_Participants" : GameElement(14, "Team_TotalParticipants.png", (1595,750,150,100)),
    "Battle_Winrate" : GameElement(15, "Battle_Winrate.png", (800,750,1120,200)),
    "Shop_Refresh" : GameElement(16, "Shop_Refresh.png", (1385,147,250,100)),
    "Select_Encounter_Reward" : GameElement(17, "Select_Encounter_Reward.png", (383, 148,850,150)),
    "RefuseGift" : GameElement(18, "RefuseGift.png", (1285,816,300,150)),
    "End_Passlvlup" : GameElement(19, "End_Passlvlup.png", (818,347,350,100)),
    "End_Victory" : GameElement(20, "End_Victory.png", (1375,150,500,500)),
    "End_ClaimTheRewards" : GameElement(21, "End_ClaimTheRewards.png", (750,450,450,200), 0.7),
    "End_ClaimTheRewards1" : GameElement(22, "End_ClaimTheRewards1.png", (750,450,450,200), 0.7),
    "End_ExplorationReward" : GameElement(23, "End_ExplorationReward.png", (725,126,400,100)),
    "End_ExplorationComplete" : GameElement(24, "End_ExplorationComplete.png", (179,112,300,200)),
    "End_Defeat" : GameElement(25, "End_Defeat.png", (1475,192,300,150)),
    "RestBonus_0" : GameElement(-2, "RestBonus_0.png", REST_BONUS_REGION, 0.95, False),
    "RestBonus_1" : GameElement(-2, "RestBonus_1.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_2" : GameElement(-2, "RestBonus_2.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_3" : GameElement(-2, "RestBonus_3.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_4" : GameElement(-2, "RestBonus_4.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_5" : GameElement(-2, "RestBonus_5.png", REST_BONUS_REGION, 0.925, False),
    "RestBonus_6" : GameElement(-2, "RestBonus_6.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_7" : GameElement(-2, "RestBonus_7.png", REST_BONUS_REGION, 0.925),
    "RestBonus_8" : GameElement(-2, "RestBonus_8.png", REST_BONUS_REGION, 0.95, False),
    "RestBonus_9" : GameElement(-2, "RestBonus_9.png", REST_BONUS_REGION, 0.9, False),
    "ResumeMD5" : GameElement(-2, "ResumeMD5.png", (781,566,400,100)),
    "Teams" : GameElement(-2, "Teams.png", (72,527,200,100)),
    "ConfirmTeam" : GameElement(-2, "ConfirmTeam.png"),
    "ConfirmBuff" : GameElement(-2, "ConfirmBuff.png"),
    "EGOGift_Confirm" : GameElement(-2, "EGOGift_Confirm.png", grayscale=False),
    "Pack_Hard" : GameElement(-2, "Pack_Hard.png", grayscale=False),
    "Pack_Hanger" : GameElement(-2, "Pack_Hanger.png", grayscale=False),
    "Clock_Face" : GameElement(-2, "Clock_Face.png", confidence=0.9, grayscale=False),
    "Enter_Node" : GameElement(-2, "Enter_Node.png", confidence=0.9, grayscale=False),
    "Event_Choices" : GameElement(-2, "Event_Choices.png", grayscale=False),
    "Event_EGOGIFT" : GameElement(-2, "Event_EGOGIFT.png", confidence=0.7, grayscale=False),
    "Event_Predicted" : GameElement(-2, "Event_Predicted.png", grayscale=False),
    "Event_VeryHigh" : GameElement(-2, "Event_VeryHigh.png", confidence=0.7, grayscale=False),
    "Event_High" : GameElement(-2, "Event_High.png", confidence=0.7, grayscale=False),
    "Event_Normal" : GameElement(-2, "Event_Normal.png", confidence=0.7, grayscale=False),
    "Event_Low" : GameElement(-2, "Event_Low.png", confidence=0.7, grayscale=False),
    "Event_VeryLow" : GameElement(-2, "Event_Low.png", confidence=0.7, grayscale=False),
    "Event_Commence" : GameElement(-2, "Event_Commence.png", grayscale=False),
    "Event_Continue" : GameElement(-2, "Event_Continue.png", grayscale=False),
    "Event_Proceed" : GameElement(-2, "Event_Proceed.png", grayscale=False),
    "Event_CommenceBattle" : GameElement(-2, "Event_CommenceBattle.png", grayscale=False),
    "Team_ClearSelection" : GameElement(-2, "Team_ClearSelection.png", confidence=0.925, grayscale=False),
    "Shop_Item" : GameElement(-2, "Shop_Item.png", (1051,325,850,700), confidence=0.935),
    "Shop_Leave" : GameElement(-2, "Shop_Leave.png", grayscale=False),
    "Reward_EGOGIFT" : GameElement(-2, "Reward_EGOGIFT.png", grayscale=False),
    "Reward_Cost" : GameElement(-2, "Reward_Cost.png", grayscale=False),
    "AcquireEGOGIFT" : GameElement(-2, "AcquireEGOGIFT.png", confidence=0.95, grayscale=False),
    "Plus1" : GameElement(-2, "Plus1.png", confidence=0.95, grayscale=False),
    "End_NoRewards" : GameElement(-2, "End_NoRewards.png", grayscale=False),
    "Shop_Item1" : GameElement(-2, "Shop_Item.png", (1051,325,850,700), confidence=0.935),
    "Shop_Item2" : GameElement(-2, "Shop_Item.png", (821,563,1150,500), confidence=0.935)
}


BASE_STATES = [
    "ClearAllCaches",
    "Drive",
    "MD5StartButton",
    "EnterMD5",
    "RestBonus",
    "DungeonProgress",
    "Starlight_Guidance",
    "Will_You_Buff",
    "Starting_Gift",
    "EGO_GIFT_GET",
    "Theme_pack",
    "NodeSelect",
    "Event_Skip",
    "Team_Total_Participants",
    "Battle_Winrate",
    "Shop_Refresh",
    "Select_Encounter_Reward",
    "RefuseGift",
    "End_Passlvlup",
    "End_Victory",
    "End_ClaimTheRewards",
    "End_ClaimTheRewards1",
    "End_ExplorationReward",
    "End_ExplorationComplete",
    "End_Defeat"
]

DEFAULT_TEAMS = [
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

class MirrorDungeonRunner:
    width: int
    height: int
    curTeam: list
    teams: list

    curState: int = -1

    def __init__(self) -> Self:
        self._get_screen_size()
        self._loadTeamConfigs()

    def _get_screen_size(self) -> None:
        self.width, self.height = pyautogui.size()

        if (self.width, self.height) != (1920, 1080):
            print("Wrong Resolution Buster")
            quit()

    def _makeConfig(self) -> None:
        with open("Config/TeamConfig.csv", 'w', newline='') as file:
            csv_writer = csv.writer(file)
            header = ["TeamRow","Type","Sinner1", "Sinner2", "Sinner3", "Sinner4", "Sinner5", "Sinner6", "Sinner7", "Sinner8", "Sinner9", "Sinner10", "Sinner11", "Sinner12"]
            csv_writer.writerows([header].extend(DEFAULT_TEAMS))

    def _loadTeamConfigs(self) -> None:
        if not os.path.exists("Config/"):
            os.makedirs("Config")
            self._makeConfig()
        elif not os.path.exists("Config/TeamConfig.csv"):
            self._makeConfig()

        with open('Config/TeamConfig.csv', 'r') as file:
            csv_reader = csv.reader(file)
            self.teams = []

            # TODO : test self.teams = csv_reader[1:] (idk if csv_reader is an iteratable, i think i can tho)
            for i, row in enumerate(csv_reader):
                if i > 0:
                    self.teams.append(row)

        self.curTeam = self.teams[0]

    def on_screen(self, game_element: GameElement) -> bool:
        image_path: str = str(IMAGE_DIR.joinpath(game_element.image))
        try:
            pyautogui.locateOnScreen(
                image_path,
                confidence=game_element.confidence,
                grayscale=game_element.grayscale,
                region=game_element.region
            )
            return True
        except:
            return False

    # Pylance say's it's return a "Box" but i can't find what lib that's from, so i'm calling it a tuple
    def locate_on_screen(self, game_element: GameElement) -> tuple | None:
        image_path: str = str(IMAGE_DIR.joinpath(game_element.image))
        try:
            return pyautogui.locateOnScreen(
                image_path,
                confidence=game_element.confidence,
                grayscale=game_element.grayscale,
                region=game_element.region
            )
        except:
            return

    def locate_all_on_screen(self, game_element: GameElement):
        image_path: str = str(IMAGE_DIR.joinpath(game_element.image))
        try:
            things = list(pyautogui.locateAllOnScreen(
                image_path,
                confidence=game_element.confidence,
                grayscale=game_element.grayscale,
                region=game_element.region
            ))
            return things
        except:
            return None

    def click_element(self, game_element: GameElement) -> bool:
        try:
            location = self.locate_on_screen(game_element)
            if not location:
                return False
            pyautogui.click(location)
            return True
        except:
            return False

    def move_to_element(self, game_element: GameElement) -> bool:
        try:
            pyautogui.moveTo(self.locate_on_screen(game_element))
            return True
        except:
            return False

    def _neutralizeMousePos(self) -> None:
        pyautogui.moveTo(self.width/2, 0)

    def find_state(self) -> int:
        for state_name in BASE_STATES:
            game_element: GameElement = GAME_ELEMENTS[state_name]

            if self.on_screen(game_element):
                if game_element.id == 1: # aka it's the drive button
                    if self.on_screen(GAME_ELEMENTS['MD5Button']):
                        return 2

                return game_element.id

        return -1

    def get_to_mirror_dungeon(self) -> None:
        while True:
            time.sleep(0.1)

            state: int = self.find_state()

            logging.debug(f'{state=}')

            match state:
                case 0:
                    pyautogui.click(self.width/2, self.height/2)
                case 1:
                    self.click_element(GAME_ELEMENTS['Drive'])
                case 2:
                    self.click_element(GAME_ELEMENTS['MD5Button'])
                case 3:
                    self.click_element(GameElement(3, "MD5StartButton.png", (715,255,550,650), 0.2))
                case 4:
                    self.click_element(GAME_ELEMENTS['EnterMD5'])
                case 6:
                    self.click_element(GAME_ELEMENTS['ResumeMD5'])
                case -1:
                    pass
                case _:
                    return

    def selectBuffs(self):
        pyautogui.click(963,727)
        pyautogui.click(682,725)
        pyautogui.click(1250,280)
        pyautogui.click(400,400)
        pyautogui.click(700,400)
        pyautogui.click(1706,991)

    def get_rest_bonus(self) -> int:
        nums = set()

        for i in range(0, 10):
            temp = self.locate_all_on_screen(GAME_ELEMENTS[f'RestBonus_{i}'])
            if temp:
                for n in temp:
                    nums.add((n.left, i))

        digitList: list = sorted(nums, reverse=True)
        returnVal = 0
        counter = 0
        for digit in digitList:
            returnVal += digit[1] * (10 ** counter)
            counter += 1

        return returnVal

    def scrollTo(self, dest: int, cur: int) -> int:
        diff: int = cur - dest
        if diff == 0:
            return cur
        baseDrag = 86

        move = baseDrag * diff / abs(diff)

        for i in range(abs(diff)):
            pyautogui.mouseDown()
            pyautogui.moveRel(0, move, duration=0.3, tween=pyautogui.easeOutQuad)
            time.sleep(0.3)
            pyautogui.mouseUp()
            pyautogui.moveRel(0, -move)

        return dest

    def selectTeam(self) -> None:
        self.move_to_element(GAME_ELEMENTS['Teams'])
        pyautogui.moveRel(0, 50)

        for i in range(30):
            pyautogui.scroll(clicks=100)

        curRow = 1
        maxBonus = 0
        maxTeamRow = 1

        for team in self.teams:
            curRow = self.scrollTo(int(team[0]), curRow)
            time.sleep(0.3)
            pyautogui.click()

            time.sleep(0.1)

            rest_bonus: int = self.get_rest_bonus()
            logging.debug(f'{curRow=} {rest_bonus=}')

            if rest_bonus > maxBonus:
                maxBonus = rest_bonus

                # TODO : get rid of id int as the first item in the list
                maxTeamRow = int(team[0])
                self.curTeam = team

        curRow = self.scrollTo(maxTeamRow, curRow)
        time.sleep(0.1)
        pyautogui.click()

        while not self.click_element(GAME_ELEMENTS['ConfirmTeam']):
            pass

        time.sleep(1)

    def selectStartingGifts(self) -> None:
        giftType: str = self.curTeam[1].lower()
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

    def run_md(self) -> None:
        while True:
            self._neutralizeMousePos()

            time.sleep(0.1)

            self.curState = self.find_state()

            logging.debug(f'{self.curState=}')

            if self.curState == -1:
                self.get_to_mirror_dungeon()

            if not self.process_state():
                break

            time.sleep(0.1)

    def do_event(self) -> None:
        if self.on_screen(GAME_ELEMENTS['Event_Choices']):
            if not self.click_element(GAME_ELEMENTS['Event_EGOGIFT']):
                pyautogui.click(1366, 350)
                pyautogui.click(1366, 600)
                pyautogui.click(1366, 750)

        # Try to click best chances
        if self.on_screen(GAME_ELEMENTS["Event_Predicted"]):
            for chance in ['VeryHigh', 'High', 'Normal', 'Low', 'VeryLow']:
                if self.click_element(GAME_ELEMENTS[f'Event_{chance}']):
                    break

        for event_state in ['Commence', 'Continue', 'Proceed', 'CommenceBattle']:
            element_name = f'Event_{event_state}'
            event_element: GameElement = GAME_ELEMENTS[element_name]

            if self.on_screen(event_element):
                if not self.click_element(event_element):
                    pyautogui.click(1707, 950)
                break

        if self.click_element(GAME_ELEMENTS['Event_Skip']):
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()

    def do_shop(self) -> None:
        for shop_name in ["Shop_Item1", "Shop_Item2"]:
            shopItems = self.locate_all_on_screen(GAME_ELEMENTS[shop_name])
            if not shopItems:
                continue

            for i in shopItems:
                pyautogui.click(i)
                time.sleep(0.75)
                pyautogui.click(1120,712)
                time.sleep(0.75)
                pyautogui.click(945,800)
                time.sleep(0.5)

        self.click_element(GAME_ELEMENTS['Shop_Leave'])
        time.sleep(0.5)
        pyautogui.click(1171,743)

    # Main MD Logic Loop
    def process_state(self) -> bool:
        match self.curState:
            case 5: # Team Selection
                if self.on_screen(GAME_ELEMENTS['Teams']):
                    self.selectTeam()
            case 7: # MD5 Buff Selection
                if self.on_screen(GAME_ELEMENTS['Starlight_Guidance']):
                    self.selectBuffs()
            case 8: # End Buff Selection
                if self.on_screen(GAME_ELEMENTS['Will_You_Buff']):
                    self.click_element(GAME_ELEMENTS['ConfirmBuff'])
            case 9: # Starting Gift Selection
                if self.on_screen(GAME_ELEMENTS['Starting_Gift']):
                    self.selectStartingGifts()
            case 10:
                if self.on_screen(GAME_ELEMENTS['EGO_GIFT_GET']):
                    self.click_element(GAME_ELEMENTS['EGOGift_Confirm'])
            case 11: # Pack Selection
                if self.on_screen(GAME_ELEMENTS['Pack_Hard']):
                    pyautogui.click(1363, 100)
                self.move_to_element(GAME_ELEMENTS['Pack_Hanger'])
                pyautogui.dragRel(0, 500, 1)
            case 12: # Node Selection
                located = False
                if self.on_screen(GAME_ELEMENTS['Clock_Face']):
                    time.sleep(0.5)
                    coords: tuple = self.locate_on_screen(GAME_ELEMENTS['Clock_Face'])
                    if coords:
                        x, y = pyautogui.center(coords)
                        pyautogui.moveTo(x, y)
                        time.sleep(0.1)
                        x += 330
                        y -= 280
                        pyautogui.click(x, y)
                        located = True

                failCounter = 0
                if located:
                    while not self.on_screen(GAME_ELEMENTS['Enter_Node']):
                        y += 300
                        pyautogui.click(x, y)
                        time.sleep(0.25)
                        failCounter += 1
                        if failCounter > 3:
                            break
                    time.sleep(0.35)
                    pyautogui.click(1704,810)
            case 13: # Event
                self.do_event()
            case 14: # Pre-fight Sinner Selection
                if self.on_screen(GAME_ELEMENTS["Team_ClearSelection"]):
                    pyautogui.click(1715, 720)
                    time.sleep(0.5)
                    pyautogui.click(1145, 740)
                    time.sleep(0.5)
                    for i in range(12):
                        pyautogui.click(SINNER_COORDINATES[self.curTeam[i+2].lower()])
                    time.sleep(0.25)
                    pyautogui.click(1720,880)
                    time.sleep(0.5)
            case 15: # OMG P-ENTER!!!
                pyautogui.click(self.width / 2, self.height / 6)
                time.sleep(0.05)
                pyautogui.press('p')
                time.sleep(0.05)
                pyautogui.press('enter')
            case 16:
                self.do_shop()
            case 17: # Ego Gift Reward 1
                if not self.click_element(GAME_ELEMENTS['Reward_EGOGIFT']):
                    self.click_element(GAME_ELEMENTS['Reward_Cost'])
                time.sleep(0.5)
                pyautogui.click(1200, 800)
            case 18: # Ego Gift Reward 2 (Acquire)
                if not self.click_element(GAME_ELEMENTS['AcquireEGOGIFT']):
                    self.click_element(GAME_ELEMENTS['Plus1'])
                time.sleep(0.2)
                pyautogui.click(1705, 870)
            case 19:
                pyautogui.click(963, 700)
                return False
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
            case 25: # Defeat Failsafe
                while True:
                    if self.on_screen(GAME_ELEMENTS['End_Defeat']):
                        pyautogui.click(1673, 840)
                    if self.on_screen(GAME_ELEMENTS['End_NoRewards']):
                        time.sleep(1)
                        pyautogui.click(1153, 740)
                        break
                    elif self.on_screen(GAME_ELEMENTS['End_ExplorationReward']):
                        pyautogui.click(587, 814)
                    elif self.on_screen(GAME_ELEMENTS['End_ExplorationComplete']):
                        pyautogui.click(1700, 900)
                    time.sleep(0.1)
        return True


