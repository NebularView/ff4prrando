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
import shutil
import requests
import re
import time

if __name__ == '__main__':
   
    # print("Validating output directories")
    # path = 'output/data/GameAssets/Serial/Data/Master'
    # isExist = os.path.exists(path)    
    # if not isExist:
    #     os.makedirs(path)
    #
    # path = 'output/data/GameAssets/Serial/Data/Message'
    # isExist = os.path.exists(path)    
    # if not isExist:
    #     os.makedirs(path)
    # print("Complete")
    

    # dataquery = dataquery(25)
    # dq = dataquery.weapontrigquery()
    # print(dq)

    #prinny = printer()
    #prinny.commandlist()
    # r1=rando()
    # r1.learningtiers()
    # exit()

    
    # r1.weaponpercen()
    # r1.weaponextras()
    # r1.armorpercen()
    # r1.armorextras()
    
    ranbool=input("Randomize types with default settings? (All) Y/N : ").upper()
    if ranbool == "Y":
        conbool="Y"
        # expbool="Y"
        chabool="Y"
        abibool="Y"
        mnbool="Y"
        armbool="Y"
        argbool="Y"
        weabool="Y"
        wegbool="Y"
        leabool="Y"
        monbool="Y"
        mncbool="Y"
        chebool="Y"
        shobool="Y"
        itebool="Y"
    else:    
        conbool=input("Adjust constants for higher maximum statistic caps and item stacks? Y/N : ").upper()
        # expbool=input("Adjust needed exp for leveling? Y/N : ").upper()
        chabool=input("Adjust character growths? Y/N : ").upper()
        abibool=input("Adjust ability strengths and mana costs? Y/N : ").upper()
        mnbool=input("Adjust monster stats? Y/N : ").upper()
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
        chebool=input("Adjust chest contents? (Very Basic Tiered) Y/N : ").upper()
        shobool=input("Adjust shop contents? (Very Basic Tiered) Y/N : ").upper()
        itebool=input("Adjust item parameters? Y/N : ").upper()
    
    varbool = input("Use default min and max variance for types? Y/N : ").upper()
    if varbool == "Y":
        chatype = "Normal" 
        abimin = 2
        abimax = 1.5
        mnmin = 2
        mnmax = 1.5
        armmin = 2
        armmax = 1.5
        weamin = 2 
        weamax = 1.5
        itemin = 2
        itemax = 1.5
        ranmode = "Normal"
    else:
        varbool2 = input("Use presets for min and max variance for types? Y/N : ").upper()
        if varbool2 == "Y":
            varbool3 = input("Select Preset: Low/Normal/High: ").upper()
            if varbool3 == "LOW":
                chatype = "Low" 
                abimin = 4
                abimax = 1
                mnmin = 1
                mnmax = 4
                armmin = 4
                armmax = 1
                weamin = 4 
                weamax = 1
                itemin = 4
                itemax = 1
                ranmode = "Low"
            elif varbool3 == "NORMAL":
                chatype = "Normal" 
                abimin = 2
                abimax = 1.5
                mnmin = 2
                mnmax = 1.5
                armmin = 2
                armmax = 1.5
                weamin = 2 
                weamax = 1.5
                itemin = 2
                itemax = 1.5
                ranmode = "Normal"
            elif varbool3 == "HIGH":
                chatype = "High" 
                abimin = 1
                abimax = 4
                mnmin = 4
                mnmax = 1
                armmin = 1
                armmax = 4
                weamin = 1 
                weamax = 4
                itemin = 1
                itemax = 4
                ranmode = "High"
        else:        
            chatype = input("Select randomization type for character growths: Low/Normal/High :").upper()
            abimin = input("Select divisor for lower bound of abilities: (Default: 2)").upper()
            abimax = input("Select multiplier for upper bound of abilities: (Default: 1.5)").upper()
            mnmin = input("Select divisor for lower bound of monster stats: (Default: 2)").upper()
            mnmax = input("Select multiplier for upper bound of monster stats: (Default: 1.5)").upper()
            armmin = input("Select divisor for lower bound of armor stats: (Default: 2)").upper()
            armmax = input("Select multiplier for upper bound of armor stats: (Default: 1.5)").upper()
            weamin = input("Select divisor for lower bound of weapon stats: (Default: 2)").upper() 
            weamax = input("Select multiplier for upper bound of weapon stats: (Default: 1.5)").upper()
            itemin = input("Select divisor for lower bound of item stats: (Default: 2)").upper()
            itemax = input("Select multiplier for upper bound of item stats: (Default: 1.5)").upper()
            ranmode = "Normal"
    
    
    
    
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

    
    print("Prepping output files")
    fileNames=file_list=os.listdir(r"Data/GameAssets/Serial/Data/Master/")
    for item in fileNames:
        if item.endswith('.csv'):
            shutil.copyfile("Data/GameAssets/Serial/Data/Master/" + item, "output/data/GameAssets/Serial/Data/Master/" + item)
    fileNames=file_list=os.listdir(r"Data/GameAssets/Serial/Data/Message/")
    for item in fileNames:
        if item.endswith('.csv'):
            shutil.copyfile("Data/GameAssets/Serial/Data/Message/" + item, "output/data/GameAssets/Serial/Data/Message/" + item)
    print("Complete")
    

    
    
    r1=rando()
    if conbool == "Y":
        print("Adjusting constants")
        r1.constadjust()
        print("Complete")
    
    # if expbool == "Y":
    #     print("Adjusting EXP values")
    #     r1.expfix()
    #     print("Complete")
    
    #r1.growthflat(hpbot="40", hptop="101", mpbot="2", mptop="80", strbot="0", strtop="3", vitbot="0", vittop="3", agibot="0", agitop="3", intbot="0", inttop="3", spibot="0", spitop="3", magbot="0", magtop="3", lukbot="0", luktop="3")
    if chabool == "Y":
        print("Adjusting growths")
        r1.growthset(chatype=chatype)
        print("Complete")
    
    if abibool == "Y":
        print("Adjusting ability strengths and mana")
        r1.abilitypercen(abimin=abimin, abimax=abimax)
        print("Complete")
        
    if mnbool == "Y":
        print("Adjusting monster stats")
        r1.monsterpercen(mnmin=mnmin, mnmax=mnmax)
        print("Complete")
    
    if armbool == "Y":
        print("Adjusting armor strengths, stats, and costs")
        r1.armorpercen(armmin=armmin, armmax=armmax)
        print("Complete")
    
    if argbool == "Y":
        print("Adjusting armor elements, procs, and group effectiveness")
        r1.armorextras()
        print("Complete")
    
    if weabool == "Y":    
        print("Adjusting weapon strengths, stats, and costs")
        r1.weaponpercen(weamin=weamin, weamax=weamax)
        print("Complete")
    
    if wegbool == "Y":
        print("Adjusting weapon elements, attributes and group effectiveness")
        r1.weaponmonextras()
        print("Complete")
    
    if leabool == "Y":
        print("Adjusting commands and spell capabilities")
        r1.learningmontiers()
        print("Complete")
    
    if monbool == "Y":
        print("Adjusting monster command descriptions")
        r1.monskillfix()
        print("Complete")
    
    if mncbool == "Y":
        print("Adjusting monster drops and steals")
        r1.monsterdropstiers()
        print("Complete")
    
    if chebool == "Y":
        print("Adjusting chest contents")
        r1.cheststiers()
        print("Complete")
    
    if shobool == "Y":
        print("Adjusting shop contents")
        r1.shopstierstypes()
        print("Complete")
        
    if itebool == "Y":
        print("Adjusting item parameters")
        r1.itempercen(itemin=itemin, itemax=itemax)
        print("Complete")
        
    print("Randomization complete, Please check output directory!")

    pass