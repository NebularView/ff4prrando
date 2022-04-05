'''
Created on Mar 16, 2022

@author: wreid
'''
import pandas as pd 
import json
from utilities.dataquery import dataquery
from utilities.printer import printer
from utilities.rando import rando
import random
from random import randrange
import os
import requests
import re
import time

if __name__ == '__main__':
   

    #prinny = printer()
    #prinny.commandlist()
    
    # r1=rando()
    # r1.weaponpercen()
    # r1.weaponextras()
    # r1.armorpercen()
    # r1.armorextras()
    ranbool=input("Randomize with default settings? (All) Y/N : ").upper()
    if ranbool == "Y":
        conbool="Y"
        expbool="Y"
        chabool="Y"
        abibool="Y"
        armbool="Y"
        argbool="Y"
        weabool="Y"
        wegbool="Y"
        leabool="Y"
        monbool="Y"
        mncbool="Y"
        chebool="Y"
    else:    
        conbool=input("Adjust constants for higher maximum statistic caps and item stacks? Y/N : ").upper()
        expbool=input("Adjust needed exp for leveling? Y/N : ").upper()
        chabool=input("Adjust character growths? Y/N : ").upper()
        abibool=input("Adjust ability strengths and mana costs? Y/N : ").upper()
        armbool=input("Adjust armor strengths, stats, and costs? Y/N : ").upper()
        if armbool == "Y":
            argbool=input("Adjust armor elements, procs, and group effectiveness? Y/N : ").upper()
        else:
            argbool="N"
        weabool=input("Adjust weapon strengths, stats, and costs? Y/N : ").upper()
        if weabool == "Y":
            wegbool=input("Adjust weapon elements, attributes and group effectiveness? Y/N : ").upper()
        else:
            wegbool="N"
        leabool=input("Adjust commands and spell capabilities? Y/N : ").upper()
        monbool=input("Adjust monster drops and steals? Y/N : ").upper()
        mncbool=input("Adjust monster command descriptions? Y/N : ").upper()
        chebool=input("Adjust chest contents? (Currently completely random and new) Y/N : ").upper()
    
    
    
 
    print("Validating output directories")
    path = 'output/data/GameAssets/Serial/Data/Master'
    isExist = os.path.exists(path)    
    if not isExist:
        os.makedirs(path)
    
    path = 'output/data/GameAssets/Serial/Data/Message'
    isExist = os.path.exists(path)    
    if not isExist:
        os.makedirs(path)
    print("Complete")
    r1=rando()
    
    
    if conbool == "Y":
        print("Adjusting constants")
        r1.constadjust()
        print("Complete")
    
    if expbool == "Y":
        print("Adjusting EXP values")
        r1.expfix()
        print("Complete")
    
    #r1.growthflat(hpbot="40", hptop="101", mpbot="2", mptop="80", strbot="0", strtop="3", vitbot="0", vittop="3", agibot="0", agitop="3", intbot="0", inttop="3", spibot="0", spitop="3", magbot="0", magtop="3", lukbot="0", luktop="3")
    if chabool == "Y":
        print("Adjusting growths")
        r1.growthset()
        print("Complete")
    
    if abibool == "Y":
        print("Adjusting ability strengths and mana")
        r1.abilitypercen()
        print("Complete")
    
    if armbool == "Y":
        print("Adjusting armor strengths, stats, and costs")
        r1.armorpercen()
        print("Complete")

    if argbool == "Y":
        print("Adjusting armor elements, procs, and group effectiveness")
        r1.armorextras()
        print("Complete")

    if weabool == "Y":    
        print("Adjusting weapon strengths, stats, and costs")
        r1.weaponpercen()
        print("Complete")

    if wegbool == "Y":
        print("Adjusting weapon elements, attributes and group effectiveness")
        r1.weaponextras()
        print("Complete")
    
    if leabool == "Y":
        print("Adjusting commands and spell capabilities")
        r1.learning()
        print("Complete")

    if monbool == "Y":
        print("Adjusting monster command descriptions")
        r1.monskillfix()
        print("Complete")
    
    if mncbool == "Y":
        print("Adjusting monster drops and steals")
        r1.monsterdrops()
        print("Complete")
    
    if chebool == "Y":
        print("Adjusting chest contents")
        r1.chests()
        print("Complete")
    
    print("Randomization complete, Please check output directory!")

    pass