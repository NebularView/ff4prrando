'''
Created on Mar 18, 2022

@author: wreid
'''

import pandas as pd 
import json
import math
from math import trunc
import random
from random import randrange
import os
import warnings
import re
from utilities.dataquery import dataquery
warnings.simplefilter(action='ignore', category=FutureWarning)

class rando:
    '''
    classdocs
    '''


    def __init__(self, **kwargs):
        
        '''
        Constructor
        '''
    def constadjust(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/game_constant_int.csv")
        for index, row in data.iterrows():
            if index <=16:
                data._set_value(index, 'value1', (row['value1']*10))
            else:
                break
        data.to_csv('output/Master/game_constant_int.csv', index=False, encoding='utf-8')

    def expfix(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/exp_table.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'total_exp', trunc(row['total_exp']/3))
    #     guids = ["1","2","3","5","6","7","8","9","10","11","12"]
    #     lvls = ["10","10","10","20","20","5","10","10","10","25","50"]
    #     exps = ["0","4","11","22","40","68","106","160","233","330","454","612","808","1050","1344","1697","2116","2611","3189","3860","4632","5517","6525","7666","8952","10396","12009","13804","15795","17996","20421","23085","26003","29191","32665","36442","40539","44973","49764","54929","60488","66461","72866","79726","87060","94891","103241","112131","121585"]
    #     s=1119
    #     f=0
    #     for guid in guids:
    #         i=1
    #         it = int(lvls[f])
    #         #print(f)
    #         #print(lvls)
    #         while i < it:
    #             new_row = {'id':s, 'type_id':1, 'group_id':guid, 'lv':i, 'total_exp':exps[i-1]}  
    #             #print(new_row) 
    #             #print(it)
    #             s += 1
    #             i += 1     
    #             data = data.append([new_row],ignore_index = True)
    #         f += 1 
        data.to_csv('output/Master/exp_table.csv', index=False, encoding='utf-8')
    #
    def growthpercen(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/growth_curve.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'hp_value1', randrange(int(row["hp_value1"]/2), int(row["hp_value1"]*2+1)))
            data._set_value(index, 'hp_value2', randrange(int(row["hp_value2"]/2), int(row["hp_value2"]*2+1)))
            data._set_value(index, 'mp_value1', randrange(int(row["mp_value1"]/2), int(row["mp_value1"]*2+1)))
            data._set_value(index, 'mp_value2', randrange(int(row["mp_value2"]/2), int(row["mp_value2"]*2+1)))
            data._set_value(index, 'strength', randrange(int(row["strength"]/2), int(row["strength"]*2+1)))
            data._set_value(index, 'vitality', randrange(int(row["vitality"]/2), int(row["vitality"]*2+1)))
            data._set_value(index, 'agility', randrange(int(row["agility"]/2), int(row["agility"]*2+1)))
            data._set_value(index, 'intelligence', randrange(int(row["intelligence"]/2), int(row["intelligence"]*2+1)))
            data._set_value(index, 'spirit', randrange(int(row["spirit"]/2), int(row["spirit"]*2+1)))
            data._set_value(index, 'magic', randrange(int(row["magic"]/2), int(row["magic"]*2+1)))
            data._set_value(index, 'luck', randrange(int(row["luck"]/2), int(row["luck"]*2+1)))
        data.to_csv('output/Master/growth_curve.csv', index=False, encoding='utf-8') 
        
    def growthflat(self, **kwargs):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/growth_curve.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'hp_value1', randrange(int(kwargs.get("hpbot")), int(kwargs.get("hptop"))+1))
            data._set_value(index, 'hp_value2', row["hp_value1"])
            data._set_value(index, 'mp_value1', randrange(int(kwargs.get("mpbot")), int(kwargs.get("mptop"))+1))
            data._set_value(index, 'mp_value2', row["mp_value1"])
            data._set_value(index, 'strength', randrange(int(kwargs.get("strbot")), int(kwargs.get("strtop"))+1))
            data._set_value(index, 'vitality', randrange(int(kwargs.get("vitbot")), int(kwargs.get("vittop"))+1))
            data._set_value(index, 'agility', randrange(int(kwargs.get("agibot")), int(kwargs.get("agitop"))+1))
            data._set_value(index, 'intelligence', randrange(int(kwargs.get("intbot")), int(kwargs.get("inttop"))+1))
            data._set_value(index, 'spirit', randrange(int(kwargs.get("spibot")), int(kwargs.get("spitop"))+1))
            data._set_value(index, 'magic', randrange(int(kwargs.get("magbot")), int(kwargs.get("magtop"))+1))
            data._set_value(index, 'luck', randrange(int(kwargs.get("lukbot")), int(kwargs.get("luktop"))+1))
        data.to_csv('output/Master/growth_curve.csv', index=False, encoding='utf-8')  

    def growthset(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/growth_curve.csv")
        for index, row in data.iterrows():
            stat=random.sample(["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1" , "1", "1", "1", "1", "1", "1", "2", "2"], 7)  
            hp = randrange(row["lv"], row["lv"]*2)
            mp = randrange(0, 20)
            data._set_value(index, 'hp_value1', hp)
            data._set_value(index, 'hp_value2', hp)
            data._set_value(index, 'mp_value1', mp)
            data._set_value(index, 'mp_value2', mp)
            data._set_value(index, 'insert_type_2', 1)
            data._set_value(index, 'strength', stat[0])
            data._set_value(index, 'vitality', stat[1])
            data._set_value(index, 'agility', stat[2])
            data._set_value(index, 'intelligence', stat[3])
            data._set_value(index, 'spirit', stat[4])
            data._set_value(index, 'magic', stat[5])
            data._set_value(index, 'luck', stat[6])
        data.to_csv('output/Master/growth_curve.csv', index=False, encoding='utf-8') 

    def abilitypercen(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/ability.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'use_value', randrange(int(row["use_value"]/2), int(row["use_value"]*2+1)))
            data._set_value(index, 'standard_value', randrange(int(row["standard_value"]/2), int(row["standard_value"]*2+1)))
        data.to_csv('output/Master/ability.csv', index=False, encoding='utf-8')  
        
    def armorpercen(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        uguid = data.equip_job_group_id.unique().tolist()
        for index, row in data.iterrows():
            gguid = random.sample(uguid, 1)
            data._set_value(index, 'equip_job_group_id', gguid[0])
            data._set_value(index, 'defense', randrange(int(row["defense"]/2), int(row["defense"]*2+1)))
            data._set_value(index, 'ability_defense', randrange(int(row["ability_defense"]/2), int(row["ability_defense"]*2+1)))
            data._set_value(index, 'weight', randrange(int(row["weight"]/2), int(row["weight"]*2+1)))
            data._set_value(index, 'evasion_rate', randrange(int(row["evasion_rate"]/2), int(row["evasion_rate"]*2+1)))
            data._set_value(index, 'ability_evasion_rate', randrange(int(row["ability_evasion_rate"]/2), int(row["ability_evasion_rate"]*2+1)))
            data._set_value(index, 'strength', randrange(abs(int(row["strength"]/2))-5, int(abs(row["strength"]*2+5))))
            data._set_value(index, 'vitality', randrange(abs(int(row["vitality"]/2))-5, int(abs(row["vitality"]*2+5))))
            data._set_value(index, 'agility', randrange(abs(int(row["vitality"]/2))-5, int(abs(row["vitality"]*2+5))))
            data._set_value(index, 'intelligence', randrange(abs(int(row["intelligence"]/2))-5, int(abs(row["intelligence"]*2+5))))
            data._set_value(index, 'spirit', randrange(abs(int(row["spirit"]/2))-5, int(abs(row["spirit"]*2+5))))
            data._set_value(index, 'magic', randrange(abs(int(row["magic"]/2))-5, int(abs(row["magic"]*2+5))))
            data._set_value(index, 'buy', randrange(abs(int(row["buy"]/5)), int(abs(row["buy"]*2+1))))
            data._set_value(index, 'sell', randrange(abs(int(row["sell"])), int(abs(row["sell"]*5+1))))
        data.to_csv('output/Master/armor.csv', index=False, encoding='utf-8') 
    
    def weaponpercen(self):
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        uguid = data.equip_job_group_id.unique().tolist()
        for index, row in data.iterrows():
            gguid = random.sample(uguid, 1)
            data._set_value(index, 'equip_job_group_id', gguid[0])
            data._set_value(index, 'attack', randrange(int(row["attack"]/2), int(row["attack"]*2+1)))
            data._set_value(index, 'weight', randrange(int(row["weight"]/2), int(row["weight"]*2+1)))
            data._set_value(index, 'strength', randrange(abs(int(row["strength"]/2))-5, int(abs(row["strength"]*2+6))))
            data._set_value(index, 'vitality', randrange(abs(int(row["vitality"]/2))-5, int(abs(row["vitality"]*2+6))))
            data._set_value(index, 'agility', randrange(abs(int(row["vitality"]/2))-5, int(abs(row["vitality"]*2+6))))
            data._set_value(index, 'intelligence', randrange(abs(int(row["intelligence"]/2))-5, int(abs(row["intelligence"]*2+6))))
            data._set_value(index, 'spirit', randrange(abs(int(row["spirit"]/2))-5, int(abs(row["spirit"]*2+6))))
            data._set_value(index, 'magic', randrange(abs(int(row["magic"]/2))-5, int(abs(row["magic"]*2+6))))
            data._set_value(index, 'buy', randrange(abs(int(row["buy"]/5)), int(abs(row["buy"]*2+1))))
            data._set_value(index, 'sell', randrange(abs(int(row["sell"])), int(abs(row["sell"]*5+1))))
        data.to_csv('output/Master/weapon.csv', index=False, encoding='utf-8') 
        
    def monskillfix(self):
        systemdata = pd.read_csv("output/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        monskilldata = pd.read_csv("Data/mon_skills.csv")
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        cq=contentdata.query('mes_id_name.str.contains("MON")')
        for id, row in cq.iterrows():
            desnameinit =  row["mes_id_name"]
            desname = re.sub("ATK", "INF", desnameinit)
            rowfind = contentdata.query('id == @row["id"]')
            rowid = rowfind["id"].index
            contentdata.loc[rowid,'mes_id_description'] = desname
            query1 = dataquery(row["mes_id_name"])
            output1 = query1.sysdataquery()
            query2 = monskilldata.query('Name.str.contains(@output1)')
            query2 = query2.head(1)
            if query2.empty == False:
                desvalue = query2['Description'].item()
                new_row = {'id':desname, 'value':desvalue}
                systemdata = systemdata.append([new_row], ignore_index = True)
        systemdata = systemdata.drop_duplicates()
        systemdata.to_csv('output/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        contentdata.to_csv('output/Master/content.csv', index=False, encoding='utf-8')
        
    def learning(self):
        jobdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/job.csv") 
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        abilitydata = pd.read_csv("output/Master/ability.csv")
        learningdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/learning.csv", nrows=0)
        charstatdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/character_status.csv")
        cq = contentdata.query('mes_id_name.str.contains("MAGIC") or mes_id_name.str.contains("MON")', engine='python')
        masterid = 1
        #print(cq)
        #print(abilitydata)
        
        for id, row in cq.iterrows():
            #print(row["type_value"])
            adq = abilitydata.query('sort_id == @row["type_value"]')
            val = adq.index.values.astype(int)[0]
            #val = int(val)
            #print(val)
            #print(abilitydata.loc[val, ])
            if abilitydata.at[val, 'type_id'] == int("4"):
                abilitydata.at[val, 'type_id'] = int("4")
            else:
                abilitydata.at[val, 'type_id'] = int("1")
            #abilitydata._set_value(val, 'type_id', int('1'))
        #print(abilitydata.dtypes)
        abilitydata.to_csv('output/Master/ability.csv', index=False, encoding='utf-8')

        
        for id, row in jobdata.iterrows():
            muser = randrange(0, 2)
            if muser == 1:
                cdq = charstatdata.query('job_id == @row["id"]')
                #print(cdq)
                if cdq.empty == False:
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "20", "22", "23", "25", "26", "27", "28", "31", "34", "0", "0", "0", "0", "0"], 2)
                    c1=str(command[0])
                    c2=str(command[1])
                    #print(cdq["id"].item())
                    #print(charstatdata)
                    #charstatdata.at[cdq["id"].item()-1, "lv"]=str("1")
                    #charstatdata.at[cdq["id"].item()-1, "exp"]=str("0")
                    #print(row)
                    if charstatdata.at[cdq["id"].item()-1, "id"] == 13:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=600
                    else:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=randrange(int(cdq["lv"]*20), int(cdq["lv"]*60))
                    charstatdata.at[cdq["id"].item()-1, "mp"]=randrange(int(cdq["lv"]*2), int(cdq["lv"]*10))
                    charstatdata.at[cdq["id"].item()-1, "strength"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "vitality"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "agility"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "intelligence"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "spirit"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "luck"]=randrange(20, 51)
                    charstatdata.at[cdq["id"].item()-1, "command_id1"]=str("1")
                    charstatdata.at[cdq["id"].item()-1, "command_id2"]=str("7")
                    charstatdata.at[cdq["id"].item()-1, "command_id3"]=c1
                    charstatdata.at[cdq["id"].item()-1, "command_id4"]=c2
                    charstatdata.at[cdq["id"].item()-1, "command_id5"]=str("3")                    
                looper=randrange(20, 51)
                #print(muser, looper)
                i = 1
                while i < looper:
                    sp = cq["id"].sample(replace=True).item()
                    lvl=randrange(1, 81)
                    #lvl=randrange(1, 151)
                    #print(sp)
                    new_row = {'id':masterid, 'type_id':1, 'value1':lvl, 'value2':0, 'job_id':row["id"], 'content_id':sp}
                    #print(new_row)
                    #learningdata = learningdata.concat(new_row, ignore_index=True)
                    
                    #print(masterid, 1, lvl, 0, jobdata["id"], sp)
                    learningdata = learningdata.append([new_row], ignore_index = True)
                    #print(learningdata)
                    i += 1
                    masterid += 1
            else:
                cdq = charstatdata.query('job_id == @row["id"]')
                if cdq.empty == False:
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "22", "23", "25", "26", "27", "31", "34", "0", "0", "0", "0", "0"], 3)
                    c1=str(command[0])
                    c2=str(command[1])
                    c3=str(command[2])
                    #print("CSTUFF" + c1, c2, c3, cdq)
                    #charstatdata.at[cdq["id"].item()-1, "lv"]=str("1")
                    #charstatdata.at[cdq["id"].item()-1, "exp"]=str("0")
                    #print(row)
                    #print(charstatdata.at[cdq["id"].item()-1, "id"])
                    if charstatdata.at[cdq["id"].item()-1, "id"] == 13:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=600
                    else:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=randrange(int(cdq["lv"]*20), int(cdq["lv"]*60))
                    charstatdata.at[cdq["id"].item()-1, "mp"]=str("0")
                    charstatdata.at[cdq["id"].item()-1, "strength"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "vitality"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "agility"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "intelligence"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "spirit"]=randrange(int(cdq["lv"]/2), int(cdq["lv"]*1.5))
                    charstatdata.at[cdq["id"].item()-1, "luck"]=randrange(20, 51)
                    charstatdata.at[cdq["id"].item()-1, "command_id1"]=str("1")
                    charstatdata.at[cdq["id"].item()-1, "command_id2"]=c1
                    charstatdata.at[cdq["id"].item()-1, "command_id3"]=c2
                    charstatdata.at[cdq["id"].item()-1, "command_id4"]=c3
                    charstatdata.at[cdq["id"].item()-1, "command_id5"]=str("3")  
        #print(learningdata)   
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        #print(systemdata)
        sdq = systemdata.query('id.str.contains("MSG_SYSTEM_089")')
        val = sdq.index.values.astype(int)[0]
        systemdata.at[val, 'value'] = 'All Magic'

        
        systemdata.to_csv('output/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        learningdata.to_csv('output/Master/learning.csv', index=False, encoding='utf-8')   
        charstatdata.to_csv('output/Master/character_status.csv', index=False, encoding='utf-8')
        #pp = printer.magiclist("bah")
        #print(pp)      