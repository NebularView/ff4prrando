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
        #Load constants file
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/game_constant_int.csv")
        for index, row in data.iterrows():
            if index <=16:
                #Adjusts values upward
                data._set_value(index, 'value1', (row['value1']*10))
            else:
                break
        #Writes File
        data.to_csv('output/data/GameAssets/Serial/Data/Master/game_constant_int.csv', index=False, encoding='utf-8')

    def expfix(self):
        #load xp table and halves required xp
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/exp_table.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'total_exp', trunc(row['total_exp']/2))
    #Played with the idea of adding levels for classes and adjusting starting levels down but seemed sketchy
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
        data.to_csv('output/data/GameAssets/Serial/Data/Master/exp_table.csv', index=False, encoding='utf-8')
    #
    def growthpercen(self):
        #Percentage based growth off of current growth values, seems like a bad idea due to split between magic/melee
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/growth_curve.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'hp_value1', randrange(int(row["hp_value1"]/2), int(row["hp_value1"]*1.5+1)))
            data._set_value(index, 'hp_value2', randrange(int(row["hp_value2"]/2), int(row["hp_value2"]*1.5+1)))
            data._set_value(index, 'mp_value1', randrange(int(row["mp_value1"]/2), int(row["mp_value1"]*1.5+1)))
            data._set_value(index, 'mp_value2', randrange(int(row["mp_value2"]/2), int(row["mp_value2"]*1.5+1)))
            data._set_value(index, 'strength', randrange(int(row["strength"]/2), int(row["strength"]*1.5+1)))
            data._set_value(index, 'vitality', randrange(int(row["vitality"]/2), int(row["vitality"]*1.5+1)))
            data._set_value(index, 'agility', randrange(int(row["agility"]/2), int(row["agility"]*1.5+1)))
            data._set_value(index, 'intelligence', randrange(int(row["intelligence"]/2), int(row["intelligence"]*1.5+1)))
            data._set_value(index, 'spirit', randrange(int(row["spirit"]/2), int(row["spirit"]*1.5+1)))
            data._set_value(index, 'magic', randrange(int(row["magic"]/2), int(row["magic"]*1.5+1)))
            data._set_value(index, 'luck', randrange(int(row["luck"]/2), int(row["luck"]*1.5+1)))
        data.to_csv('output/data/GameAssets/Serial/Data/Master/growth_curve.csv', index=False, encoding='utf-8') 
        
    def growthflat(self, **kwargs):
        #Growth based of input variables
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
        data.to_csv('output/data/GameAssets/Serial/Data/Master/growth_curve.csv', index=False, encoding='utf-8')  

    def growthset(self):
        #Growth based off of a set of values that should mimic the actual growth curve (if a little below)
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
        data.to_csv('output/data/GameAssets/Serial/Data/Master/growth_curve.csv', index=False, encoding='utf-8') 

    def abilitypercen(self):
        #Adjust ability power and mp cost by percent
        data = pd.read_csv("output/data/GameAssets/Serial/Data/Master/ability.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'use_value', randrange(int(row["use_value"]/2), int(row["use_value"]*1.5+1)))
            data._set_value(index, 'standard_value', randrange(int(row["standard_value"]/2), int(row["standard_value"]*1.5+1)))
        data.to_csv('output/data/GameAssets/Serial/Data/Master/ability.csv', index=False, encoding='utf-8')  
        
    def armorpercen(self):
        #Adjusts columns listed below by percent for armor
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        uguid = data.equip_job_group_id.unique().tolist()
        for index, row in data.iterrows():
            gguid = random.sample(uguid, 1)
            data._set_value(index, 'equip_job_group_id', gguid[0])
            data._set_value(index, 'defense', randrange(int(row["defense"]/2), int(row["defense"]*1.5+1)))
            data._set_value(index, 'ability_defense', randrange(int(row["ability_defense"]/2), int(row["ability_defense"]*1.5+1)))
            data._set_value(index, 'weight', randrange(int(row["weight"]/2), int(row["weight"]*1.5+1)))
            data._set_value(index, 'evasion_rate', randrange(int(row["evasion_rate"]/2), int(row["evasion_rate"]*1.5+1)))
            data._set_value(index, 'ability_evasion_rate', randrange(int(row["ability_evasion_rate"]/2), int(row["ability_evasion_rate"]*1.5+1)))
            data._set_value(index, 'strength', randrange(abs(int(row["strength"]/2))-1, int(abs(row["strength"]*1.5+1))))
            data._set_value(index, 'vitality', randrange(abs(int(row["vitality"]/2))-1, int(abs(row["vitality"]*1.5+1))))
            data._set_value(index, 'agility', randrange(abs(int(row["vitality"]/2))-1, int(abs(row["vitality"]*1.5+1))))
            data._set_value(index, 'intelligence', randrange(abs(int(row["intelligence"]/2))-1, int(abs(row["intelligence"]*1.5+1))))
            data._set_value(index, 'spirit', randrange(abs(int(row["spirit"]/2))-1, int(abs(row["spirit"]*1.5+1))))
            data._set_value(index, 'magic', randrange(abs(int(row["magic"]/2))-1, int(abs(row["magic"]*1.5+1))))
            if row["buy"] == 0:
                if row["defense"] == 0:
                    data._set_value(index, 'buy', randrange(1000, 50000))
                    data._set_value(index, 'sell', int(trunc(row["buy"])/2))   
                else:
                    data._set_value(index, 'buy', randrange(abs(int(row["defense"]*1000)), int(abs(row["defense"]*2000))))
                    data._set_value(index, 'sell', int(trunc(row["buy"])/2))
            else:
                data._set_value(index, 'buy', randrange(abs(int(row["buy"]/2+1)), int(abs(row["buy"]*2+2))))
                data._set_value(index, 'sell', int(row["buy"])/2)
        data.to_csv('output/data/GameAssets/Serial/Data/Master/armor.csv', index=False, encoding='utf-8') 
    
    def armorextras(self):
        #Implementation is bad, however this will randomize the resistances, the protected conditions and the species effectiveness of armor
        data = pd.read_csv("output/data/GameAssets/Serial/Data/Master/armor.csv")
        #Needs a template
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])

        res_att = data.resistance_attribute.unique().tolist()
        res_con = data.resistance_condition.unique().tolist()
        res_spe = data.resistance_species.unique().tolist()
        res_att.remove(0)
        res_con.remove(0)
        res_spe.remove(0)
        # print(res_att)
        # print(res_con)
        # print(res_spe)
        # From here on be dragons
        for index, row in data.iterrows():
            dq = dataquery(row["id"])
            #print(row["id"])
            sysval = dq.armordataquery()
            output = None
            #print(sysval)            
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_att, 1)
                data._set_value(index, 'resistance_attribute', guid[0])
                dq = dataquery(guid[0])
                #print(dq.armorelemquery())
                if output == None:
                    output = dq.elemquery() + ' - '
                else:
                    output += dq.elemquery() + ' - '
                del dq
            else:
                data._set_value(index, 'resistance_attribute', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_con, 1)
                data._set_value(index, 'resistance_condition', guid[0])
                dq = dataquery(guid[0])
                #print(dq.condquery())
                if output == None:
                    output = dq.condquery() + ' - '
                else:
                    output += dq.condquery() + ' - '
                del dq
            else:
                data._set_value(index, 'resistance_condition', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_spe, 1)
                data._set_value(index, 'resistance_species', guid[0])
                #print(guid[0])
                dq = dataquery(guid[0])
                #print(dq.specquery())
                if output == None:
                    output = dq.specquery() + ' - '
                else:
                    output += dq.specquery() + ' - '
                del dq
            else:
                data._set_value(index, 'resistance_species', '0')
            if output != None:
                dq = dataquery(row["id"])
                sysdata = re.sub('NAME', 'INF', dq.armordataquery())
                sdq = systemdata.query("id == @sysdata")
                systemdata._set_value(sdq.index.values[0], 'value', output.rstrip(" - "))
                #print(sdq.index.values[0])
                #print(output)
            else:
                dq = dataquery(row["id"])
                sysdata = re.sub('NAME', 'INF', dq.armordataquery())
                sdq = systemdata.query("id == @sysdata")
                #print(sdq.index.values[0])
                systemdata._set_value(sdq.index.values[0], 'value', "No Special Values")
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        data.to_csv('output/data/GameAssets/Serial/Data/Master/armor.csv', index=False, encoding='utf-8')

    def itempercen(self):
        #Items by percentages
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/item.csv")
        for index, row in data.iterrows():
            data._set_value(index, 'standard_value', randrange(int(row["standard_value"]/2), int(row["standard_value"]*1.5+1)))
            if row["buy"] == 0:
                #Completely arbitrary at the moment
                data._set_value(index, 'buy', randrange(1000, 5000))
                data._set_value(index, 'sell', trunc(int(row["buy"])/2))
            else:
                #Completely arbitrary at the moment
                data._set_value(index, 'buy', randrange(abs(int(row["buy"]/2+1)), int(abs(row["buy"]*2+2))))
                data._set_value(index, 'sell', trunc(int(row["buy"])/2))
            data._set_value(index, 'sales_not_possible', 0)
        data.to_csv('output/data/GameAssets/Serial/Data/Master/item.csv', index=False, encoding='utf-8')                 
    
    def weaponpercen(self):
        #Weapons by percentages
        data = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        uguid = data.equip_job_group_id.unique().tolist()
        for index, row in data.iterrows():
            gguid = random.sample(uguid, 1)
            data._set_value(index, 'equip_job_group_id', gguid[0])
            data._set_value(index, 'attack', randrange(int(row["attack"]/2), int(row["attack"]*1.5+1)))
            data._set_value(index, 'weight', randrange(int(row["weight"]/2), int(row["weight"]*1.5+1)))
            data._set_value(index, 'strength', randrange(int(row["strength"]/2)-1, int(abs(row["strength"]*1.5+1))))
            data._set_value(index, 'vitality', randrange(int(row["vitality"]/2)-1, int(abs(row["vitality"]*1.5+1))))
            data._set_value(index, 'agility', randrange(int(row["vitality"]/2)-1, int(abs(row["vitality"]*1.5+1))))
            data._set_value(index, 'intelligence', randrange(int(row["intelligence"]/2)-1, int(abs(row["intelligence"]*1.5+1))))
            data._set_value(index, 'spirit', randrange(int(row["spirit"]/2)-1, int(abs(row["spirit"]*1.5+1))))
            data._set_value(index, 'magic', randrange(int(row["magic"]/2)-1, int(abs(row["magic"]*1.5+1))))
            if row["buy"] == 0:
                if row["attack"] == 0:
                    #Completely arbitrary at the moment
                    data._set_value(index, 'buy', randrange(1000, 5000))
                    data._set_value(index, 'sell', int(trunc(row["buy"])/2))                    
                else:
                    #Completely arbitrary at the moment
                    data._set_value(index, 'buy', randrange(abs(int(row["attack"]*1000)), int(abs(row["attack"]*2000))))
                    data._set_value(index, 'sell', int(trunc(row["buy"])/2))
            else:
                data._set_value(index, 'buy', randrange(abs(int(row["buy"]/2+1)), int(abs(row["buy"]*2+2))))
                data._set_value(index, 'sell', int(row["buy"])/2)
        data.to_csv('output/data/GameAssets/Serial/Data/Master/weapon.csv', index=False, encoding='utf-8') 

    def weaponextras(self):
        #More in depth than armor: Trigger, weak attribute, effective species, conditions, and attributes
        data = pd.read_csv("output/data/GameAssets/Serial/Data/Master/weapon.csv")
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        contentdata.query('mes_id_name.str.contains("MAGIC") and mes_id_battle.str.contains("None")', engine='python')
        res_tri = data.trigger_ability_id.unique().tolist()
        res_wat = data.weak_attribute.unique().tolist()
        res_esp = data.effective_species.unique().tolist()
        res_add = data.additional_condition_group_id.unique().tolist()
        #Still not sure what this does?
        res_att = data.attribute_id.unique().tolist()
        res_tri.remove(0)
        res_wat.remove(0)
        res_esp.remove(0)
        res_add.remove(0)
        res_att.remove(0)
        for index, row in data.iterrows():
            output = None
            dq = dataquery(row["id"])
            #print(row["id"])
            sysval = dq.weapondataquery()
            #print(sysval)
            output = None
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_tri, 1)
                data._set_value(index, 'trigger_ability_id', guid[0])
                dq = dataquery(guid[0])
                #print(dq.magicdataquery2())
                if output == None:
                    output = "On Use: " + dq.magicdataquery2() + ' - '
                else:
                    output += "On Use: " + dq.magicdataquery2() + ' - '
                del dq
            else:
                data._set_value(index, 'trigger_ability_id', '0')
            #b = randrange(0, 8)
            # if b == 1:
            #     guid = random.sample(res_wat, 1)
            #     data._set_value(index, 'weak_attribute', guid[0])
            #     dq = dataquery('guid[0]')
            #     if output == None:
            #         output = dq.contentdataquery() + ' - '
            #     else:
            #         output += dq.contentdataquery() + ' - '
            #     del dq
            # else:
            #     data._set_value(index, 'weak_attribute', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_esp, 1)
                data._set_value(index, 'effective_species', guid[0])
                #print(guid[0])
                dq = dataquery(guid[0])
                if output == None:
                    output = dq.specquery() + ' - '
                else:
                    output += dq.specquery() + ' - '
                del dq
            else:
                data._set_value(index, 'effective_species', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_add, 1)
                data._set_value(index, 'additional_condition_group_id', guid[0])
                dq = dataquery(guid[0])
                if output == None:
                    output = dq.condquery() + ' - '
                else:
                    output += dq.condquery() + ' - '
                del dq
            else:
                data._set_value(index, 'additional_condition_group_id', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_att, 1)
                data._set_value(index, 'attribute_id', guid[0])
                data._set_value(index, 'attribute_group_id', guid[0]+100)
                data._set_value(index, 'weak_attribute', guid[0])
                dq = dataquery(guid[0]+100)
                if output == None:
                    output = dq.elemquery() + ' - '
                else:
                    output += dq.elemquery() + ' - '
                del dq
            else:
                data._set_value(index, 'attribute_id', '0')
                data._set_value(index, 'attribute_group_id', '0')
                data._set_value(index, 'weak_attribute', '0')
            #print(output)
            if output != None:
                dq = dataquery(row["id"])
                #print(dq.weapondataquery())
                sysdata = re.sub('NAME', 'INF', dq.weapondataquery())
                #print(sysdata)
                sdq = systemdata.query("id == @sysdata")
                systemdata._set_value(sdq.index.values[0], 'value', output.rstrip(" - "))
                #print(sdq.index.values[0])
                #print(output)
            else:
                dq = dataquery(row["id"])
                sysdata = re.sub('NAME', 'INF', dq.weapondataquery())
                #print(sysdata)
                sdq = systemdata.query("id == @sysdata")
                #print(sdq.index.values[0])
                systemdata._set_value(sdq.index.values[0], 'value', "No Special Values")
        systemdata._set_value(1252, 'value', "Empty")
        systemdata._set_value(1253, 'value', "None")
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        data.to_csv('output/data/GameAssets/Serial/Data/Master/weapon.csv', index=False, encoding='utf-8')
        
    def weaponmonextras(self):
        #Same as above however trigger abilities can contain monster skills
        data = pd.read_csv("output/data/GameAssets/Serial/Data/Master/weapon.csv")
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        contentdata.query('mes_id_name.str.contains("MAGIC") and mes_id_battle.str.contains("None")', engine='python')
        spelltierlist = pd.read_csv("Data/Extra/spec_spell_tier.csv")
        res_wat = data.weak_attribute.unique().tolist()
        res_esp = data.effective_species.unique().tolist()
        res_add = data.additional_condition_group_id.unique().tolist()
        res_att = data.attribute_id.unique().tolist()
        res_wat.remove(0)
        res_esp.remove(0)
        res_add.remove(0)
        res_att.remove(0)
        for index, row in data.iterrows():
            output = None
            dq = dataquery(row["id"])
            #print(row["id"])
            sysval = dq.weapondataquery()
            #print(sysval)
            output = None
            b = randrange(0, 8)
            if b == 1:
                if row["sort_id"] < 25:
                    res_tri = spelltierlist.query("tier == 1")
                elif row["sort_id"] < 50:
                    res_tri = spelltierlist.query("tier == 2")
                elif row["sort_id"] < 75:
                    res_tri = spelltierlist.query("tier == 3")
                elif row["sort_id"] < 100:
                    res_tri = spelltierlist.query("tier == 4")
                guid = res_tri["ab_id"].sample(replace=True).item()
                data._set_value(index, 'trigger_ability_id', guid)
                spq = spelltierlist.query("ab_id == @guid")
                pspq = spq["sys_name"].item()
                #print(pspq)
                
                #print(dq.magicdataquery2())
                if output == None:
                    output = "On Use: " + pspq + ' - '
                else:
                    output += "On Use: " + pspq + ' - '
                del dq
            else:
                data._set_value(index, 'trigger_ability_id', '0')
            #b = randrange(0, 8)
            # if b == 1:
            #     guid = random.sample(res_wat, 1)
            #     data._set_value(index, 'weak_attribute', guid[0])
            #     dq = dataquery('guid[0]')
            #     if output == None:
            #         output = dq.contentdataquery() + ' - '
            #     else:
            #         output += dq.contentdataquery() + ' - '
            #     del dq
            # else:
            #     data._set_value(index, 'weak_attribute', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_esp, 1)
                data._set_value(index, 'effective_species', guid[0])
                #print(guid[0])
                dq = dataquery(guid[0])
                if output == None:
                    output = dq.specquery() + ' - '
                else:
                    output += dq.specquery() + ' - '
                del dq
            else:
                data._set_value(index, 'effective_species', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_add, 1)
                data._set_value(index, 'additional_condition_group_id', guid[0])
                dq = dataquery(guid[0])
                if output == None:
                    output = dq.condquery() + ' - '
                else:
                    output += dq.condquery() + ' - '
                del dq
            else:
                data._set_value(index, 'additional_condition_group_id', '0')
            b = randrange(0, 8)
            if b == 1:
                guid = random.sample(res_att, 1)
                data._set_value(index, 'attribute_id', guid[0])
                data._set_value(index, 'attribute_group_id', guid[0]+100)
                data._set_value(index, 'weak_attribute', guid[0])
                dq = dataquery(guid[0]+100)
                if output == None:
                    output = dq.elemquery() + ' - '
                else:
                    output += dq.elemquery() + ' - '
                del dq
            else:
                data._set_value(index, 'attribute_id', '0')
                data._set_value(index, 'attribute_group_id', '0')
                data._set_value(index, 'weak_attribute', '0')
            #print(output)
            if output != None:
                dq = dataquery(row["id"])
                #print(dq.weapondataquery())
                sysdata = re.sub('NAME', 'INF', dq.weapondataquery())
                #print(sysdata)
                sdq = systemdata.query("id == @sysdata")
                systemdata._set_value(sdq.index.values[0], 'value', output.rstrip(" - "))
                #print(sdq.index.values[0])
                #print(output)
            else:
                dq = dataquery(row["id"])
                sysdata = re.sub('NAME', 'INF', dq.weapondataquery())
                #print(sysdata)
                sdq = systemdata.query("id == @sysdata")
                #print(sdq.index.values[0])
                systemdata._set_value(sdq.index.values[0], 'value', "No Special Values")
        systemdata._set_value(1252, 'value', "Empty")
        systemdata._set_value(1253, 'value', "None")
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        data.to_csv('output/data/GameAssets/Serial/Data/Master/weapon.csv', index=False, encoding='utf-8')
        
        
    def monskillfix(self):
        #This section pulls in a created mon_skills.csv to populate detail data for skills
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        monskilldata = pd.read_csv("Data/Extra/mon_skills.csv")
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
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        contentdata.to_csv('output/data/GameAssets/Serial/Data/Master/content.csv', index=False, encoding='utf-8')
        
    def learning(self):
        #this is a doozy
        #Loading Needed Files
        jobdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/job.csv") 
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        abilitydata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/ability.csv")
        learningdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/learning.csv", nrows=0)
        charstatdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/character_status.csv")
        #Query to determine what qualifies as a magic based on message string
        cq = contentdata.query('mes_id_name.str.contains("MAGIC") and mes_id_battle.str.contains("None")', engine='python')
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
                #Preserve needed commands/abilities
                abilitydata.at[val, 'type_id'] = int("4")
            else:
                #Everything else castable as black magic
                abilitydata.at[val, 'type_id'] = int("2")
            #abilitydata._set_value(val, 'type_id', int('1'))
        #print(abilitydata.dtypes)
        abilitydata.to_csv('output/data/GameAssets/Serial/Data/Master/ability.csv', index=False, encoding='utf-8')

        
        for id, row in jobdata.iterrows():
            #Determine if magic user (50/50)
            muser = randrange(0, 2)
            if row["id"] == 4:
                muser = 0
            if muser == 1:
                #pull char data
                cdq = charstatdata.query('job_id == @row["id"]')
                #print(cdq)
                #shitty error handling i know
                if cdq.empty == False:
                    #Pull two commands from list of command numbers
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "20", "22", "23", "25", "26", "27", "28", "31", "34", "0", "0", "0", "0", "0"], 2)
                    command.sort(reverse=True)
                    c1=str(command[0])
                    c2=str(command[1])
                    #print(cdq["id"].item())
                    #print(charstatdata)
                    #charstatdata.at[cdq["id"].item()-1, "lv"]=str("1")
                    #charstatdata.at[cdq["id"].item()-1, "exp"]=str("0")
                    #print(row)
                    #fix for paladin cecil going blep
                    if charstatdata.at[cdq["id"].item()-1, "id"] == 13:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=600
                    else:
                        charstatdata.at[cdq["id"].item()-1, "hp"]=randrange(int(cdq["lv"]*20), int(cdq["lv"]*60))
                    #Randomize starting stats and commands
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
                #Here be spells.  20-50 is completely arbitrary
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
                #If you ain't a magic user
                cdq = charstatdata.query('job_id == @row["id"]')
                if cdq.empty == False:
                    #3 commands instead of two
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "22", "23", "25", "26", "27", "31", "34", "0", "0", "0", "0", "0"], 3)
                    command.sort(reverse=True)
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
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        #print(systemdata)
        sdq = systemdata.query('id.str.contains("MSG_SYSTEM_089")')
        #print(systemdata)
        val = sdq.index.values.astype(int)[0]
        #Create "All Magic" from black magic
        systemdata.at[val, 'value'] = 'All Magic'

        
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        learningdata.to_csv('output/data/GameAssets/Serial/Data/Master/learning.csv', index=False, encoding='utf-8')   
        charstatdata.to_csv('output/data/GameAssets/Serial/Data/Master/character_status.csv', index=False, encoding='utf-8')
        #pp = printer.magiclist("bah")
        #print(pp)      

    def learningtiers(self):
        #same as above with tiered spells (pretty arbitrary)
        jobdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/job.csv") 
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        abilitydata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/ability.csv")
        learningdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/learning.csv", nrows=0)
        charstatdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/character_status.csv")
        cq = contentdata.query('mes_id_name.str.contains("MAGIC") and mes_id_battle.str.contains("None")', engine='python')
        spelltierlist = pd.read_csv("Data/Extra/spell_tier.csv")
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
                abilitydata.at[val, 'type_id'] = int("2")
            #abilitydata._set_value(val, 'type_id', int('1'))
        #print(abilitydata.dtypes)
        abilitydata.to_csv('output/data/GameAssets/Serial/Data/Master/ability.csv', index=False, encoding='utf-8')

        
        for id, row in jobdata.iterrows():
            muser = randrange(0, 2)
            if muser == 1:
                cdq = charstatdata.query('job_id == @row["id"]')
                #print(cdq)
                if cdq.empty == False:
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "20", "22", "23", "25", "26", "27", "28", "31", "34", "0", "0", "0", "0", "0"], 2)
                    command.sort(reverse=True)
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
                    charstatdata.at[cdq["id"].item()-1, "command_id2"]=str("8")
                    charstatdata.at[cdq["id"].item()-1, "command_id3"]=c1
                    charstatdata.at[cdq["id"].item()-1, "command_id4"]=c2
                    charstatdata.at[cdq["id"].item()-1, "command_id5"]=str("3")                    
                looper=randrange(20, 51)
                #print(muser, looper)
                i = 1
                spq1 = spelltierlist.query("tier == 1")
                spq2 = spelltierlist.query("tier == 2")  
                spq3 = spelltierlist.query("tier == 3")  
                spq4 = spelltierlist.query("tier == 4")
                while i < looper:
                    
                    #Meat that does spell tiering pulled from list of spells in the Extras folder
                    lvl=randrange(1, 81)
                    if lvl < 15:
                        sp = spq1["con_id"].sample(replace=False).item()
                    elif lvl < 30:
                        sp = spq2["con_id"].sample(replace=False).item()                        
                    elif lvl < 45:
                        sp = spq3["con_id"].sample(replace=False).item()                        
                    elif lvl < 60:
                        sp = spq4["con_id"].sample(replace=False).item()                        
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
                    command.sort(reverse=True)
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
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        #print(systemdata)
        sdq = systemdata.query('id.str.contains("MSG_SYSTEM_092")')
        #print(systemdata)
        val = sdq.index.values.astype(int)[0]
        systemdata.at[val, 'value'] = 'All Magic'

        
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        learningdata.to_csv('output/data/GameAssets/Serial/Data/Master/learning.csv', index=False, encoding='utf-8')   
        charstatdata.to_csv('output/data/GameAssets/Serial/Data/Master/character_status.csv', index=False, encoding='utf-8')
        #pp = printer.magiclist("bah")
        #print(pp)    
        

    def learningmontiers(self):
        #Learning but with monster skills
        jobdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/job.csv") 
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        abilitydata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/ability.csv")
        learningdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/learning.csv", nrows=0)
        charstatdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/character_status.csv")
        cq = contentdata.query('(mes_id_name.str.contains("MAGIC") or mes_id_name.str.contains("MON")) and mes_id_battle.str.contains("None")', engine='python')
        spelltierlist = pd.read_csv("Data/Extra/spell_tier.csv")
        monspelltierlist = pd.read_csv("Data/Extra/spec_spell_tier.csv")
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
                abilitydata.at[val, 'type_id'] = int("2")
            #abilitydata._set_value(val, 'type_id', int('1'))
        #print(abilitydata.dtypes)
        abilitydata.to_csv('output/data/GameAssets/Serial/Data/Master/ability.csv', index=False, encoding='utf-8')

        
        for id, row in jobdata.iterrows():
            #Muser adjusted upward, still 50% change to be magic user
            muser = randrange(0, 101)
            if muser <= 50:
                cdq = charstatdata.query('job_id == @row["id"]')
                #print(cdq)
                if cdq.empty == False:
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "20", "22", "23", "25", "26", "27", "28", "31", "34", "0", "0", "0", "0", "0"], 2)
                    command.sort(reverse=True)
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
                    charstatdata.at[cdq["id"].item()-1, "command_id2"]=str("8")
                    charstatdata.at[cdq["id"].item()-1, "command_id3"]=c1
                    charstatdata.at[cdq["id"].item()-1, "command_id4"]=c2
                    charstatdata.at[cdq["id"].item()-1, "command_id5"]=str("3")                    
                looper=randrange(20, 51)
                #print(muser, looper)
                i = 1
                spq1 = spelltierlist.query("tier == 1")
                spq2 = spelltierlist.query("tier == 2")  
                spq3 = spelltierlist.query("tier == 3")  
                spq4 = spelltierlist.query("tier == 4")
                while i < looper:
                    lvl=randrange(1, 81)
                    if lvl < 15:

                        sp = spq1["con_id"].sample(replace=False).item()
                    elif lvl < 30:

                        sp = spq2["con_id"].sample(replace=False).item()                        
                    elif lvl < 45:
                        
                        sp = spq3["con_id"].sample(replace=False).item()                        
                    elif lvl < 60:

                        sp = spq4["con_id"].sample(replace=False).item()                        
                    #lvl=randrange(1, 151)
                    #print(sp)
                    #print("test" + str(sp))
                    new_row = {'id':masterid, 'type_id':1, 'value1':lvl, 'value2':0, 'job_id':row["id"], 'content_id':sp}
                    #print(new_row)
                    #learningdata = learningdata.concat(new_row, ignore_index=True)
                    
                    #print(masterid, 1, lvl, 0, jobdata["id"], sp)
                    learningdata = learningdata.append([new_row], ignore_index = True)
                    #print(learningdata)
                    i += 1
                    masterid += 1
            #1% chance to cast monster skills
            elif muser >= 100: 
                print("Special Monster Spells: " + str(row["id"]))
                cdq = charstatdata.query('job_id == @row["id"]')
                #print(cdq)
                if cdq.empty == False:
                    command=random.sample(["10", "11", "12", "13", "14", "16", "17", "19", "20", "22", "23", "25", "26", "27", "28", "31", "34", "0", "0", "0", "0", "0"], 2)
                    command.sort(reverse=True)
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
                    charstatdata.at[cdq["id"].item()-1, "command_id2"]=str("8")
                    charstatdata.at[cdq["id"].item()-1, "command_id3"]=c1
                    charstatdata.at[cdq["id"].item()-1, "command_id4"]=c2
                    charstatdata.at[cdq["id"].item()-1, "command_id5"]=str("3")                    
                looper=randrange(20, 51)
                #print(muser, looper)
                i = 1
                spq1 = monspelltierlist.query("tier == 1")
                spq2 = monspelltierlist.query("tier == 2")
                spq3 = monspelltierlist.query("tier == 3")
                spq4 = monspelltierlist.query("tier == 4")
                while i < looper:

                    lvl=randrange(1, 81)
                    if lvl < 15:                        
                        sp = spq1["con_id"].sample(replace=False).item()
                    elif lvl < 30:
                        sp = spq2["con_id"].sample(replace=False).item()                        
                    elif lvl < 45:
                        sp = spq3["con_id"].sample(replace=False).item()                        
                    elif lvl < 60:
                        sp = spq4["con_id"].sample(replace=False).item()                        
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
                    command.sort(reverse=True)
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
        systemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        #print(systemdata)
        sdq = systemdata.query('id.str.contains("MSG_SYSTEM_092")')
        #print(systemdata)
        val = sdq.index.values.astype(int)[0]
        systemdata.at[val, 'value'] = 'All Magic'

        
        systemdata.to_csv('output/data/GameAssets/Serial/Data/Message/system_en.txt', index=False, header=False, sep='\t', encoding='utf-8')
        learningdata.to_csv('output/data/GameAssets/Serial/Data/Master/learning.csv', index=False, encoding='utf-8')   
        charstatdata.to_csv('output/data/GameAssets/Serial/Data/Master/character_status.csv', index=False, encoding='utf-8')
        #pp = printer.magiclist("bah")
        #print(pp)        

        
    def chests(self):
        #Chest randomization
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        cq = contentdata.query('mes_id_name.str.contains("ARMOR") or mes_id_name.str.contains("WEAPON") or mes_id_name.str.contains("ITEM")', engine='python')
        #sp = cq["id"].sample(replace=True).item()
        #Inside of the entity_default.json if the content_id field exists, that is the item denotation
        for root, dirs, files in os.walk("data"):
            for file in files:
                #print(root, dirs, file)
                if file.startswith("entity_default.json"):
                    m = open(root + "/" + file)
                    map = json.load(m)
                    for i in map['layers']:
                        for j in i['objects']:
                            for k in j['properties']:
                                if k['name'] == 'content_id':
                                    sp = cq["id"].sample(replace=True).item()
                                    k['value'] = sp
                                    #print(k['name'], k['value'])
                    isExist = os.path.exists("output\\" + root)    
                    #print("output\\" + root)
                    if not isExist:
                        os.makedirs("output\\" + root)
                    
                    out_file = open("output\\" + root + "\\" + file, "w")
                    
                    json.dump(map, out_file)
                    out_file.close()

    def cheststiers(self):
        itemtierdata = pd.read_csv("Data/Extra/item_tier.csv")
        maptierdata = pd.read_csv("Data/Extra/map_tier.csv")
        #sp = cq["id"].sample(replace=True).item()
        
        #Enhanced logic for item tiers,     
        for root, dirs, files in os.walk("data"):
            for file in files:
                #print(root, dirs, file)
                if file.startswith("entity_default.json"):
                    m = open(root + "/" + file)
                    map = json.load(m)
                    for i in map['layers']:
                        for j in i['objects']:
                            for k in j['properties']:
                                if k['name'] == 'content_id':
                                    #print(mapdata)
                                    m=os.path.basename(os.path.normpath(root))
                                    #print(m)
                                    mtier=maptierdata.query('map_name == @m')
                                    mtier=mtier["tier"].item()
                                    #print(mtier)
                                    if mtier == 1:
                                        itier=itemtierdata.query('tier == @mtier')
                                        itier2=itemtierdata.query('tier == @mtier')
                                        itier3=itemtierdata.query('tier == @mtier+1')
                                        itier4=itemtierdata.query('tier == @mtier+1')
                                    elif mtier == 9:
                                        itier=itemtierdata.query('tier == @mtier')
                                        itier2=itemtierdata.query('tier == @mtier')
                                        itier3=itemtierdata.query('tier == @mtier-1')
                                        itier4=itemtierdata.query('tier == @mtier-1')
                                    else:
                                        itier=itemtierdata.query('tier == @mtier')
                                        itier2=itemtierdata.query('tier == @mtier')
                                        itier3=itemtierdata.query('tier == @mtier-1')
                                        itier4=itemtierdata.query('tier == @mtier+1')
                                    sampler = itier["id"].to_list() + itier2["id"].to_list() + itier3["id"].to_list() + itier4["id"].to_list()
                                    #print(sampler)
                                    #print(m)
                                    sp = random.sample(sampler, 1)[0]
                                    #print(sp)
                                    k['value'] = sp
                                #This is for gil and was causing some issues
                                if k['name'] == 'content_num':
                                    k['value'] = 1
                                #I need to tweak this a bit further, this is the message that appears when you open 03 is ??? GIL which i wanted to get rid of, but still seeing it in grass chests
                                if k['name'] == 'message_key': 
                                    if k['value'] == "S0005_999_a_03":
                                        k['value'] = 'S0005_999_a_02'
                                    #print(k['name'], k['value'])
                    isExist = os.path.exists("output\\" + root)    
                    #print("output\\" + root)
                    if not isExist:
                        os.makedirs("output\\" + root)
                    
                    out_file = open("output\\" + root + "\\" + file, "w")
                    
                    json.dump(map, out_file)
                    out_file.close()

    def monsterdrops(self):
        #Randomizes monster drops
        monsterdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/monster.csv")
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        cq = contentdata.query('mes_id_name.str.contains("ARMOR") or mes_id_name.str.contains("WEAPON") or mes_id_name.str.contains("ITEM")', engine='python')
        for id, row in monsterdata.iterrows():
            if row['id'] == 185:
                pass
            else:
                if row['drop_content_id1'] != 0:
                    sp = cq["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id1', sp)
                    sp = cq["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id2', sp)
                    sp = cq["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id3', sp)
                    sp = cq["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id4', sp)
                    sp = cq["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id5', sp)
        monsterdata.to_csv('output/data/GameAssets/Serial/Data/Master/monster.csv', index=False, encoding='utf-8')
        

    def monsterdropstiers(self):
        #Tiered version of above
        monsterdata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/monster.csv")
        itemtierdata = pd.read_csv("Data/Extra/item_tier.csv")
        for id, row in monsterdata.iterrows():
            #DAMNIT LUGAE, only stupid monster that drops a key item
            if row['id'] == 185:
                pass
            else:
                if row['drop_content_id1'] != 0:
                    if trunc(row['lv']/10)==0:
                        mtier=1
                    else:
                        mtier=trunc(row['lv']/10)
                    itier=itemtierdata.query('tier == @mtier')
                    sp = itier["id"].sample(replace=True).item()                
                    monsterdata._set_value(id, 'drop_content_id1', sp)
                    sp = itier["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id2', sp)
                    sp = itier["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id3', sp)
                    sp = itier["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id4', sp)
                    sp = itier["id"].sample(replace=True).item()
                    monsterdata._set_value(id, 'drop_content_id5', sp)
        monsterdata.to_csv('output/data/GameAssets/Serial/Data/Master/monster.csv', index=False, encoding='utf-8')
        
    def monsterpercen(self):
        #Tiered version of above
        monsterdata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/monster.csv")
        #Weapons by percentages
        for index, row in monsterdata.iterrows():
            monsterdata._set_value(index, 'defense', randrange(int(row["defense"]/2), int(row["defense"]*1.5+1)))
            monsterdata._set_value(index, 'ability_defense', randrange(int(row["ability_defense"]/2), int(row["ability_defense"]*1.5+1)))
            monsterdata._set_value(index, 'hp', randrange(int(row["hp"]/2), int(row["hp"]*1.5+1)))
            monsterdata._set_value(index, 'mp', randrange(int(row["mp"]/2), int(abs(row["mp"]*1.5+1))))
            monsterdata._set_value(index, 'exp', randrange(int(row["exp"]*1.5), int(abs(row["exp"]*4+1))))
            monsterdata._set_value(index, 'gill', row["gill"]*4)
            monsterdata._set_value(index, 'attack', randrange(int(row["attack"]/2), int(row["attack"]*1.5+1)))
            monsterdata._set_value(index, 'agility', randrange(int(row["agility"]/2), int(row["agility"]*1.5+1)))
            monsterdata._set_value(index, 'intelligence', randrange(int(row["intelligence"]/2), int(row["intelligence"]*1.5+1)))
            monsterdata._set_value(index, 'spirit', randrange(int(row["spirit"]/2), int(abs(row["spirit"]*1.5+1))))
            monsterdata._set_value(index, 'magic', randrange(int(row["magic"]/2), int(abs(row["magic"]*1.5+1))))
        monsterdata.to_csv('output/data/GameAssets/Serial/Data/Master/monster.csv', index=False, encoding='utf-8')



    def shops(self):
        #SHop randomization
        productdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv")
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        weapondata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/weapon.csv")
        armordata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/armor.csv")
        itemdata = pd.read_csv("output/data/GameAssets/Serial/Data/Master/item.csv")
        cq = contentdata.query('mes_id_name.str.contains("ARMOR") or mes_id_name.str.contains("WEAPON") or mes_id_name.str.contains("ITEM")', engine='python')
        pq = productdata.query('content_id != 0')
        pq2 = productdata.query('content_id == 0')
        producttemp = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv", nrows=0)
        shops = pq.group_id.unique().tolist()
        masterid = 1
        
        for shop in shops:
            num=randrange(1, 21)
            i=1
            while i < num:
                sp = cq["id"].sample(replace=True).item()
                new_row = {'id':masterid, 'content_id':sp, 'group_id':shop, 'coefficient':0, 'purchase_limit':0}
                producttemp = producttemp.append([new_row], ignore_index = True)
                i += 1
                masterid +=1
        
        for id, row in pq2.iterrows():
            #print(row)
            row._set_value("id", masterid)
            #print(row)
            producttemp = producttemp.append([row], ignore_index = True)
            masterid +=1
        
        producttemp.to_csv('output/data/GameAssets/Serial/Data/Master/product.csv', index=False, encoding='utf-8')
        for id, row in weapondata.iterrows():
            if row.empty == False:
                if row['buy'] == 0:
                    weapondata._set_value(id, 'buy', 1)
        for id, row in armordata.iterrows():
            if row.empty == False:
                if row['buy'] == 0:
                    armordata._set_value(id, 'buy', 1)
        for id, row in itemdata.iterrows():    
            #print(row)
            if row.empty == False:
                if row['buy'] == 0:
                    itemdata._set_value(id, 'buy', 1)
        armordata.to_csv('output/data/GameAssets/Serial/Data/Master/armor.csv', index=False, encoding='utf-8')
        weapondata.to_csv('output/data/GameAssets/Serial/Data/Master/weapon.csv', index=False, encoding='utf-8')
        itemdata.to_csv('output/data/GameAssets/Serial/Data/Master/item.csv', index=False, encoding='utf-8')
        
    def shopstiers(self):
        #Shop tiered randomization
        productdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv")
        #maptierdata = pd.read_csv("Data/map_tier.csv")
        itemtierdata = pd.read_csv("Data/Extra/item_tier.csv")
        pq = productdata.query('content_id != 0')
        pq2 = productdata.query('content_id == 0')
        producttemp = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv", nrows=0)
        shops = pq.group_id.unique().tolist()
        masterid = 1
        
        for shop in shops:
            if shop == 0:
                tier=1
            elif shop <5: 
                tier=1
            elif shop <10:
                tier=2
            elif shop <15:
                tier=3
            elif shop <20:
                tier=4
            elif shop <25:
                tier=5
            elif shop <30:
                tier=6
            elif shop <35:
                tier=7
            elif shop <38:
                tier=8
            elif shop <100:
                tier=9

            #print(tier)
            #print(tier)
            if tier == 1:
                itier=itemtierdata.query('tier == @tier')
                itier2=itemtierdata.query('tier == @tier')
                itier3=itemtierdata.query('tier == @tier+1')
                itier4=itemtierdata.query('tier == @tier+1')
            elif tier == 9:
                itier=itemtierdata.query('tier == @tier')
                itier2=itemtierdata.query('tier == @tier')
                itier3=itemtierdata.query('tier == @tier-1')
                itier4=itemtierdata.query('tier == @tier-1')
            else:
                itier=itemtierdata.query('tier == @tier')
                itier2=itemtierdata.query('tier == @tier')
                itier3=itemtierdata.query('tier == @tier-1')
                itier4=itemtierdata.query('tier == @tier+1')
            sampler = itier["id"].to_list() + itier2["id"].to_list() + itier3["id"].to_list() + itier4["id"].to_list()
            num=randrange(5, 16)
            i=1
            while i < num:
                sp = random.sample(sampler, 1)[0]
                new_row = {'id':masterid, 'content_id':sp, 'group_id':shop, 'coefficient':0, 'purchase_limit':0}
                producttemp = producttemp.append([new_row], ignore_index = True)
                i += 1
                masterid +=1
        
        for id, row in pq2.iterrows():
            #print(row)
            row._set_value("id", masterid)
            #print(row)
            producttemp = producttemp.append([row], ignore_index = True)
            masterid +=1
        
        producttemp.to_csv('output/data/GameAssets/Serial/Data/Master/product.csv', index=False, encoding='utf-8')

    def shopstierstypes(self):
        #Shop tiered randomization
        productdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv")
        shoptierdata = pd.read_csv("Data/Extra/shop_tier.csv")
        #maptierdata = pd.read_csv("Data/map_tier.csv")
        itemtierdata = pd.read_csv("Data/Extra/item_tier.csv")
        pq2 = productdata.query('content_id == 0')
        producttemp = pd.read_csv("Data/GameAssets/Serial/Data/Master/product.csv", nrows=0)
        masterid = 1
        
        for index, row in shoptierdata.iterrows():
            tier = row["tier"]
            itype = row["type"]
            shop = row["group_id"]
            if tier == 1:
                itier=itemtierdata.query('tier == @tier and type == @itype')
                itier2=itemtierdata.query('tier == @tier and type == @itype')
                itier3=itemtierdata.query('tier == @tier+1 and type == @itype')
                itier4=itemtierdata.query('tier == @tier+1 and type == @itype')
                new_row = {'id':masterid, 'content_id':2, 'group_id':shop, 'coefficient':0, 'purchase_limit':0}
                producttemp = producttemp.append([new_row], ignore_index = True)
                new_row = {'id':masterid, 'content_id':21, 'group_id':shop, 'coefficient':0, 'purchase_limit':0}
                producttemp = producttemp.append([new_row], ignore_index = True)
            elif tier == 9:
                itier=itemtierdata.query('tier == @tier and type == @itype')
                itier2=itemtierdata.query('tier == @tier and type == @itype')
                itier3=itemtierdata.query('tier == @tier-1 and type == @itype')
                itier4=itemtierdata.query('tier == @tier-1 and type == @itype')
            else:
                itier=itemtierdata.query('tier == @tier and type == @itype')
                itier2=itemtierdata.query('tier == @tier and type == @itype')
                itier3=itemtierdata.query('tier == @tier-1 and type == @itype')
                itier4=itemtierdata.query('tier == @tier+1 and type == @itype')
            sampler = itier["id"].to_list() + itier2["id"].to_list() + itier3["id"].to_list() + itier4["id"].to_list()
            num=randrange(2, 8)
            i=1
            while i < num:
                sp = random.sample(sampler, 1)[0]
                new_row = {'id':masterid, 'content_id':sp, 'group_id':shop, 'coefficient':0, 'purchase_limit':0}
                producttemp = producttemp.append([new_row], ignore_index = True)
                i += 1
                masterid +=1
        
        for id, row in pq2.iterrows():
            #print(row)
            row._set_value("id", masterid)
            #print(row)
            producttemp = producttemp.append([row], ignore_index = True)
            masterid +=1
        
        producttemp.to_csv('output/data/GameAssets/Serial/Data/Master/product.csv', index=False, encoding='utf-8')

        
            