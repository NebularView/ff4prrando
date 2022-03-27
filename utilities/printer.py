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
        print("fuck")
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