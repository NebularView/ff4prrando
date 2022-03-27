'''
Created on Mar 16, 2022

@author: wreid
'''
import pandas as pd 
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
 
    print("Validating output directories")
    path = 'output/Master'
    isExist = os.path.exists(path)    
    if not isExist:
        os.makedirs(path)
    
    path = 'output/Message'
    isExist = os.path.exists(path)    
    if not isExist:
        os.makedirs(path)
    print("Complete")
    r1=rando()
    print("Adjusting constants")
    r1.constadjust()
    print("Complete")
    
    print("Adjusting EXP values")
    r1.expfix()
    print("Complete")
    
    #r1.growthflat(hpbot="40", hptop="101", mpbot="2", mptop="80", strbot="0", strtop="3", vitbot="0", vittop="3", agibot="0", agitop="3", intbot="0", inttop="3", spibot="0", spitop="3", magbot="0", magtop="3", lukbot="0", luktop="3")
    print("Adjusting growths")
    r1.growthset()
    print("Complete")
    
    print("Adjusting ability strengths and mana")
    r1.abilitypercen()
    print("Complete")
    
    print("Adjusting armor strengths, stats, and costs")
    r1.armorpercen()
    print("Complete")
    
    print("Adjusting weapon strengths, stats, and costs")
    r1.weaponpercen()
    print("Complete")
    
    print("Adjusting commands and spell capabilities")
    r1.learning()
    print("Complete")
    
    print("Adjusting monster command descriptions")
    r1.monskillfix()
    print("Complete")

    # systemdata = pd.read_csv("output/Message/system_en.txt", delimiter='\t', names=['id', 'value'], encoding='utf-8')
    # monskilldata = pd.read_csv("Data/mon_skills.csv")
    # contentdata = pd.read_csv("output/Master/content.csv", encoding='utf-8')
    # print(contentdata["mes_id_description"])
    # print(contentdata["mes_id_name"])
    # cq=contentdata.query('mes_id_name.str.contains("MON")', engine="python")
    #
    # for id, row in cq.iterrows():
    #     desnameinit =  row["mes_id_name"]
    #     desname = re.sub("ATK", "INF", desnameinit)
    #     rowfind = contentdata.query('id == @row["id"]')
    #     rowid = rowfind["id"].index
    #     contentdata.loc[rowid,'mes_id_description'] = desname
    #     query1 = dataquery(row["mes_id_name"])
    #     output1 = query1.sysdataquery()
    #     query2 = monskilldata.query('Name.str.contains(@output1)')
    #     query2 = query2.head(1)
    #     if query2.empty == False:
    #         desvalue = query2['Description'].item()
    #         new_row = {'id':desname, 'value':desvalue}
    #         systemdata = systemdata.append([new_row], ignore_index = True)
    # systemdata = systemdata.drop_duplicates()
    # systemdata.to_csv('output/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8', mode='w+')
    # contentdata.to_csv('output/Master/content.csv', index=False, encoding='utf-8')
    #
    # # time.sleep(5)
    # #
    # # print("Adjusting monster command descriptions")
    # # r1.monskillfix()
    # # print("Complete")
    
    print("Randomization complete!")

    pass