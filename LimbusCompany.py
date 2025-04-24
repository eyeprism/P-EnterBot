import pathlib
import logging
import time

from dataclasses import dataclass
from typing import Self, overload

import pyautogui

logging.basicConfig(level=logging.DEBUG)

IMAGE_DIR = pathlib.Path('Images/')

@dataclass
class GameElement:
    id: int
    image: str
    region: tuple[int, int, int, int]
    confidence: float = 0.8
    grayscale: bool = True

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
    "Event_Skip" : GameElement(13, "Event_Skip.png", (849,443,150,100)),
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
    "RestBonus_0" : GameElement(-1, "RestBonus_0.png", REST_BONUS_REGION, 0.95, False),
    "RestBonus_1" : GameElement(-1, "RestBonus_1.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_2" : GameElement(-1, "RestBonus_2.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_3" : GameElement(-1, "RestBonus_3.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_4" : GameElement(-1, "RestBonus_4.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_5" : GameElement(-1, "RestBonus_5.png", REST_BONUS_REGION, 0.925, False),
    "RestBonus_6" : GameElement(-1, "RestBonus_6.png", REST_BONUS_REGION, 0.9, False),
    "RestBonus_7" : GameElement(-1, "RestBonus_7.png", REST_BONUS_REGION, 0.925),
    "RestBonus_8" : GameElement(-1, "RestBonus_8.png", REST_BONUS_REGION, 0.95, False),
    "RestBonus_9" : GameElement(-1, "RestBonus_9.png", REST_BONUS_REGION, 0.9, False),
    "ResumeMD5" : GameElement(-1, "ResumeMD5.png", (781,566,400,100))
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

class LimbusCompany:
    width: int
    height: int

    def __init__(self) -> Self:
        self._get_screen_size()

    def _get_screen_size(self) -> None:
        self.width, self.height = pyautogui.size()

        if (self.width, self.height) != (1920, 1080):
            print("Wrong Resolution Buster")
            quit()

    @overload
    def on_screen(self, image: str, confidence: float | None = 0.999, grayscale: bool | None = True, region: tuple[int, int, int, int] | None = (0,0,1920,1080)) -> bool:
        image_path: pathlib.Path = IMAGE_DIR.joinpath(image)
        try:
            pyautogui.locateOnScreen(
                image_path,
                confidence=confidence,
                grayscale=grayscale,
                region=region
            )
            return True
        except:
            return False

    @overload
    def on_screen(self, game_element: GameElement) -> bool:
        image_path: pathlib.Path = IMAGE_DIR.joinpath(game_element.image)
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
        image_path: pathlib.Path = IMAGE_DIR.joinpath(game_element.image)
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
        image_path: pathlib.Path = IMAGE_DIR.joinpath(game_element.image)
        try:
            return pyautogui.locateAllOnScreen(
                image_path,
                confidence=game_element.confidence,
                grayscale=game_element.grayscale,
                region=game_element.region
            )
        except:
            return

    def click_element(self, game_element: GameElement) -> bool:
        try:
            pyautogui.click(self.locate_on_screen(game_element))
            return True
        except:
            return False

    def _neutralizeMousePos(self) -> None:
        pyautogui.moveTo(self.width/2, 0)

    def find_state(self) -> int:
        for state_name in BASE_STATES:
            game_element: GameElement = GAME_ELEMENTS[state_name]

            if self.on_screen(game_element):
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
                case 5:
                    self.click_element(GAME_ELEMENTS['ResumeMD5'])
                case -1:
                    pass
                case _:
                    return

    def get_rest_bonus(self) -> int:
        nums = set()

        for i in range(0, 10):
            if (temp := self.locate_all_on_screen(GAME_ELEMENTS[f'RestBonus_{i}'])):
                for n in temp:
                    nums.add((n.left, i))

        digitList: list = sorted(nums, reverse=True)
        returnVal = 0
        counter = 0
        for digit in digitList:
            returnVal += digit[1] * (10 ** counter)

