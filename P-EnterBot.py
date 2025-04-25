import multiprocessing
import argparse
import time
import os

import pyautogui
import keyboard

import LimbusCompany

parser = argparse.ArgumentParser(
    prog="(L.C.M.D.D.S) : Limbus Company Mirror Dungeon Do-er Script"
)
parser.add_argument('-r', '--runs', type=int)

pyautogui.FAILSAFE = False

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

args = parser.parse_args()

def main():
    runs = 0
    if not args.runs:
        user_input = pyautogui.prompt(text = "Enter number of MD runs", title = "StartMenu", default = 1)
        if type(user_input) != int:
            print("Number of runs must be integer")
            exit(1)
    else:
        runs = args.runs

    mirror_dungeon_runner = LimbusCompany.MirrorDungeonRunner()
    for i in range(runs):
        mirror_dungeon_runner.run_md()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    process = multiprocessing.Process(target=main)#multiprocess with main function so failsafe key can be detected whenever
    process.start()
    while process.is_alive():
        time.sleep(0.1)
        if keyboard.is_pressed('q'): #failsafe
            process.terminate()
            break
