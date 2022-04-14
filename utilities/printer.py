'''
Created on Mar 18, 2022

@author: wreid
'''
import pandas as pd
from utilities.dataquery import dataquery

class printer(object):
    '''
    classdocs
    '''


    def __init__(self):
                '''
        Constructor
        '''
    
    def commandlist(self):
        commanddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/command.csv")
        for index, row in commanddata.iterrows():

            query1 = dataquery(row["mes_id_name"])
            output1 = query1.sysdataquery()
            if output1 != "None":
                print(str(row["id"]) + ", " + str(output1))
                
            else:
                return
            
    def itemlist(self):
        itemdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/item.csv")
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        for index, row in itemdata.iterrows():

            query1 = dataquery(row["id"])
            output1 = query1.itemdataquery()
            if output1 != "None":
                print(str(output1))
                
            
        for index, row in armordata.iterrows():

            query2 = dataquery(row["id"])
            output2 = query2.armordataquery()
            if output2 != "None":
                print(str(output2))
                
            
        for index, row in weapondata.iterrows():

            query3 = dataquery(row["id"])
            output3 = query3.weapondataquery()
            if output3 != "None":
                print(str(output3))
                
                

    def magiclist(self):
        #learningdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/learning.csv")
        learningdata = pd.read_csv("output/learning.csv")
#       contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        jobdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/job.csv")
#       systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        charstatdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/character_status.csv")
        
        for id, row in learningdata.iterrows():
            output3 = row['value1'].item()
            cid = row['content_id'].item()
            jid = row['job_id'].item()
            jout = jobdata.query('id == @jid')
            jobmes = jout['mes_id_name'].item()
            query1 = dataquery(cid)
            output1 = query1.contentdataquery()
            query2 = dataquery(jobmes)
            output2 = query2.sysdataquery()
            print(output2, output3, output1)
    pass
    def abilitylist(self):
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        abilitydata = pd.read_csv("Data/GameAssets/Serial/Data/Master/ability.csv")
        cdq = contentdata.query('(mes_id_name.str.contains("MAGIC") or mes_id_name.str.contains("MON")) and mes_id_battle.str.contains("None")', engine='python')
        #print(cdq)
        for id, row in cdq.iterrows():
            abq = abilitydata.query('id == @row["type_value"]')
            query = dataquery(row["mes_id_name"])
            #print(abq)
            if abq.iloc[0]["use_value"] != 0:
                print (str(abq.iloc[0]["id"]) + ", " + str(abq.iloc[0]["use_value"]) + ", " + str(abq.iloc[0]["standard_value"]) + ", " + str(row["id"]) + ", " + query.sysdataquery())
    pass
    def charcommandlist(self):
        charstatdata = pd.read_csv("output/character_status.csv")
        commanddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/command.csv")
        for index, row in charstatdata.iterrows():

            query1 = dataquery(row["mes_id_name"])
            output1 = query1.sysdataquery()
            if output1 == "None":
                return
            mes1 = commanddata.query('id == @row["command_id1"]')
        
            if mes1.empty:
                output2 = "No Command"
            else:
                mes1add = mes1["id"].item()
                mes1 = mes1["mes_id_name"].item()
                query2 = dataquery(mes1)
                output2 = query2.sysdataquery()
                output2 += " - " + str(mes1add)
            mes2 = commanddata.query('id == @row["command_id2"]')
        
            if mes2.empty:
                output3 = "No Command"
            else:
                mes2add = mes2["id"].item()
                mes2 = mes2["mes_id_name"].item()
                query3 = dataquery(mes2)
                output3 = query3.sysdataquery()
                output3 += " - " + str(mes2add)
            mes3 = commanddata.query('id == @row["command_id3"]')
        
            if mes3.empty:
                output4 = "No Command"
            else:
                mes3add = mes3["id"].item()
                mes3 = mes3["mes_id_name"].item()
                query4 = dataquery(mes3)
                output4 = query4.sysdataquery()
                output4 += " - " + str(mes3add)
            mes4 = commanddata.query('id == @row["command_id4"]')
            if mes4.empty:            
                output5 = "No Command"
            else:
                mes4add = mes4["id"].item()
                mes4 = mes4["mes_id_name"].item()
                query5 = dataquery(mes4)
                output5 = query5.sysdataquery()
                output5 += " - " + str(mes4add)
            mes5 = commanddata.query('id == @row["command_id5"]')
        
            if mes5.empty:
                output6 = "No Command"
            else:
                mes5add = mes5["id"].item()
                mes5 = mes5["mes_id_name"].item()
                query6 = dataquery(mes5)
                output6 = query6.sysdataquery()
                output6 += " - " + str(mes5add)
    
            print(str(output1) + "\n" + "----------\n" + str(output2) + "\n" + str(output3) + "\n" + str(output4) + "\n" + str(output5) + "\n" + str(output6) + "\n")
            
            
    def condlist(self):
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        condgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition_group.csv")
        conddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition.csv")
        
        for index, row in condgdata.iterrows():
            #print(row)
            output1 = "None"
            query1 = conddata.query('id == @row["condition_id"]')
            #print(query1["mes_id_name"].item())
            if query1["mes_id_name"].item() != 'None':
                #print(query1["mes_id_name"])
                query1 = dataquery(query1["mes_id_name"].item())
                output1 = str(row["condition_id"].item()) + " - " + query1.sysdataquery()
            if output1 != "None":
                print(str(output1))
                
    def armorcondlist(self):
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        condgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition_group.csv")
        conddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition.csv")
        
        #print(armordata.info())

        for index, row in armordata.iterrows():
            output3 = "Resistances: \n"
            if row["resistance_condition"] != 0:
                tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["resistance_condition"])
                query1 = condgdata.loc[condgdata['group_id'] == row["resistance_condition"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['condition_id']
                    #print(index)
                    query2 = conddata.loc[conddata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["mes_id_name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        if i == 0:
                            output3 += output2 + " :"
                        query3 = dataquery(query2["mes_id_name"].item())
                        output3 = output3 + " " + query3.sysdataquery()
                    i += 1
                if output3 != "None":
                    print(str(output3))
