'''
Created on Mar 18, 2022

@author: wreid
'''
import pandas as pd 
import re

class dataquery:
    '''
    classdocs
    '''


    def __init__(self, value):
        
        self.value = value
        
    def contentdataquery(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('id == @self.value')
    
        #print (cq)
    
        q2 = cq['mes_id_name'].item()
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = sq['value'].item()
        
        return(sdout)
                 
        pass

    def contentdataqueryability(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        print(self.value)
        cq = contentdata.query('type_id == 4 and type_value == @self.value')
    
        #print (cq)
        print(cq)
        q2 = cq['mes_id_name'].item()
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = sq['value'].item()
        
        return(sdout)
                 
        pass

    def sysdataquery(self):
        
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        sq = systemdata.query('id == @self.value')
    
        #print (sq)
    
        if sq.empty == False:
            sdout = sq['value'].item()
            return(sdout)
                 
        pass
    
    def itemdataquery(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('type_value == @self.value and type_id == 1')
    
        #print (cq)
    
        q2 = cq['mes_id_name'].item()
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = str(cq['id'].item()) + ', ' + sq['value'].item()
        
        return(sdout)
                 
        pass
    
    def weapondataquery(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('type_value == @self.value and type_id == 2')
    
        #print (cq)
    
        q2 = cq['mes_id_name'].item()
        
        #print(q2)
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = str(sq['id'].item())
        
        return(sdout)
                 
        pass
    
    
    def magicdataquery(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('type_value == @self.value and type_id == 4')
    
        #print (cq)
        
        #print(cq)
    
        q2 = cq['mes_id_name'].item()
        
        #print(q2)
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = str(sq['id'].item())
        
        return(sdout)
                 
        pass

    def magicdataquery2(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('type_value == @self.value and type_id == 4')
    
        #print (cq)
        
        #print(cq['mes_id_name'])
    
        q2 = cq['mes_id_name'].item()
        
        #print(q2)
    
        #print (q2)
    
        sq = systemdata.query('id == @q2')
    
        #print (sq)
    
        sdout = re.sub('<.*>', '', str(sq['value'].item()))
        #print(sdout)
        
        return(sdout)
                 
        pass

    def armordataquery(self):
        
        contentdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/content.csv")
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        cq = contentdata.query('type_value == @self.value and type_id == 3')
        
        #print(cq)
    
        #print (cq)
    
        q2 = cq['mes_id_name'].item()
        
        
        #print(q2)
    
        sq = systemdata.query('id == @q2')
    
        #print(sq)
    
        sdout = str(sq['id'].item())
        
        return(sdout)
                 
        pass
        '''
        Constructor
        '''

    def armorcondquery(self):
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        condgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition_group.csv")
        conddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition.csv")
        aq = armordata.query('id == @self.value')
        
        

        for index, row in aq.iterrows():
            output3 = "Resistances:"
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
                        #if i == 0:
                            #output3 += output2 + " :"
                        query3 = dataquery(query2["mes_id_name"].item())
                        output3 = output3 + " " + query3.sysdataquery()
                    i += 1
                if output3 != "None":
                    return(str(output3))         
                  
    def armorattrquery(self):
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        attrgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/attribute_group.csv")
        elemdata = pd.read_csv("Data/Extra/element.csv")
        aq = armordata.query('id == @self.value')
        
        

        for index, row in aq.iterrows():
            output3 = "Elements:"
            if row["resistance_attribute"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["resistance_attribute"])
                query1 = attrgdata.loc[attrgdata['group_id'] == row["resistance_attribute"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['attribute_id']
                    #print(index)
                    query2 = elemdata.loc[elemdata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        #if i == 0:
                            #output3 += output2 + " :"
                        output3 = output3 + " " + query2["name"].item()
                    i += 1
                if output3 != "None":
                    return(str(output3))
                
    def armorspecquery(self):
        armordata = pd.read_csv("Data/GameAssets/Serial/Data/Master/armor.csv")
        specgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/species_group.csv")
        specdata = pd.read_csv("Data/Extra/species.csv")
        aq = armordata.query('id == @self.value')
        
        

        for index, row in aq.iterrows():
            output3 = "Species:"
            if row["resistance_species"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["resistance_species"])
                query1 = specgdata.loc[specgdata['group_id'] == row["resistance_species"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['species_id']
                    #print(index)
                    query2 = specdata.loc[specdata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        #if i == 0:
                            #output3 += output2 + " :"
                        output3 = output3 + " " + query2["name"].item()
                    i += 1
                if output3 != "None":
                    return(str(output3))
                

    def weaponcondquery(self):
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        condgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition_group.csv")
        conddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition.csv")
        wq = weapondata.query('id == @self.value')
        
        

        for index, row in wq.iterrows():
            output3 = "On Hit:"
            if row["additional_condition_group_id"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["additional_condition_group_id"])
                query1 = condgdata.loc[condgdata['group_id'] == row["additional_condition_group_id"]]
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
                        #if i == 0:
                            #output3 += output2 + " :"
                        query3 = dataquery(query2["mes_id_name"].item())
                        output3 = output3 + " " + query3.sysdataquery()
                    i += 1
                if output3 != "None":
                    return(str(output3))
                
                
    def weaponattrquery(self):
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        attrgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/attribute_group.csv")
        elemdata = pd.read_csv("Data/Extra/element.csv")
        wq = weapondata.query('id == @self.value')
        
        

        for index, row in wq.iterrows():
            #print(row)
            output3 = "Elements:"
            if row["attribute_group_id"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["attribute_group_id"])
                query1 = attrgdata.loc[attrgdata['group_id'] == row["attribute_group_id"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['attribute_id']
                    #print(index)
                    query2 = elemdata.loc[elemdata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        #if i == 0:
                            #output3 += output2 + " :"
                        output3 = output3 + " " + query2["name"].item()
                    i += 1
                if output3 != "None":
                    return(str(output3))

    def weaponweakattrquery(self):
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        attrgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/attribute_group.csv")
        elemdata = pd.read_csv("Data/Extra/element.csv")
        wq = weapondata.query('id == @self.value')
        
        

        for index, row in wq.iterrows():
            #print(row)
            output3 = "Weak Elements:"
            if row["weak_attribute"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["weak_attribute"])
                query1 = attrgdata.loc[attrgdata['group_id'] == row["weak_attribute"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['attribute_id']
                    #print(index)
                    query2 = elemdata.loc[elemdata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        #if i == 0:
                            #output3 += output2 + " :"
                        output3 = output3 + " " + query2["name"].item()
                    i += 1
                if output3 != "None":
                    return(str(output3))

    def weaponspecquery(self):
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        specgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/species_group.csv")
        specdata = pd.read_csv("Data/Extra/species.csv")
        wq = weapondata.query('id == @self.value')
        
        

        for index, row in wq.iterrows():
            output3 = "Species:"
            if row["effective_species"] != 0:
                #tester = str(row.resistance_condition)
                #print(row["resistance_condition"])
                #print(condgdata["id"])
                #query1 = condgdata.query('id == 82')
                output2 = str(row["effective_species"])
                query1 = specgdata.loc[specgdata['group_id'] == row["effective_species"]]
                #print(query1)
                i=0
                for index, row in query1.iterrows():
                    #print(row)
                    
                    output1 = row['species_id']
                    #print(index)
                    query2 = specdata.loc[specdata['id'] == output1]
                    #print(query1["mes_id_name"].item())
                    if query2["name"].item() != 'None':
                        #print(query1["mes_id_name"])
                        #if i == 0:
                            #output3 += output2 + " :"
                        output3 = output3 + " " + query2["name"].item()
                    i += 1
                if output3 != "None":
                    return(str(output3))
                
    def weapontrigquery(self):
        weapondata = pd.read_csv("Data/GameAssets/Serial/Data/Master/weapon.csv")
        ability = pd.read_csv("Data/GameAssets/Serial/Data/Master/ability.csv")
        wq = weapondata.query('id == @self.value')
        #print(wq)
        

        for index, row in wq.iterrows():
            #print(row)
            wdq = dataquery(row['trigger_ability_id'])
            output1 = "On Use: " + re.sub('<.*>', '', wdq.magicdataquery()) 
            if output1 != "None":
                return(str(output1))

    def trigquery(self):
        wdq = dataquery(self.value)
        ability = pd.read_csv("Data/GameAssets/Serial/Data/Master/ability.csv")
        output1 = "On Use: " + re.sub('<.*>', '', wdq.magicdataquery()) 
        return(str(output1))
            
    def elemquery(self):
        attrgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/attribute_group.csv")
        elemdata = pd.read_csv("Data/Extra/element.csv")
        output3 = "Elements:"
        if self.value != 0:
            #tester = str(row.resistance_condition)
            #print(row["resistance_condition"])
            #print(condgdata["id"])
            #query1 = condgdata.query('id == 82')
            output2 = str(self.value)
            #print(self.value)
            query1 = attrgdata.loc[attrgdata['group_id'] == self.value]
            #print(query1)
            i=0
            for index, row in query1.iterrows():
                #print(row)
                
                output1 = row['attribute_id']
                #print(index)
                query2 = elemdata.loc[elemdata['id'] == output1]
                #print(query1["mes_id_name"].item())
                if query2["name"].item() != 'None':
                    #print(query1["mes_id_name"])
                    #if i == 0:
                        #output3 += output2 + " :"
                    output3 = output3 + " " + query2["name"].item()
                i += 1
            if output3 != "None":
                return(str(output3))      
            
    def condquery(self):       
        condgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition_group.csv")
        conddata = pd.read_csv("Data/GameAssets/Serial/Data/Master/condition.csv")
        

        output3 = "Status:"
        if self.value != 0:
            #tester = str(row.resistance_condition)
            #print(row["resistance_condition"])
            #print(condgdata["id"])
            #query1 = condgdata.query('id == 82')
            output2 = str(self.value)
            query1 = condgdata.loc[condgdata['group_id'] == self.value]
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
                    #if i == 0:
                        #output3 += output2 + " :"
                    query3 = dataquery(query2["mes_id_name"].item())
                    output3 = output3 + " " + query3.sysdataquery()
                i += 1
            if output3 != "None":
                return(str(output3))


    def specquery(self):
        specgdata = pd.read_csv("Data/GameAssets/Serial/Data/Master/species_group.csv")
        specdata = pd.read_csv("Data/Extra/species.csv")       
        
        output3 = "Species:"
        if self.value != 0:
            #tester = str(row.resistance_condition)
            #print(row["resistance_condition"])
            #print(condgdata["id"])
            #query1 = condgdata.query('id == 82')
            output2 = str(self.value)
            query1 = specgdata.loc[specgdata['group_id'] == self.value]
            #print(query1)
            i=0
            for index, row in query1.iterrows():
                #print(row)
                
                output1 = row['species_id']
                #print(output1)
                query2 = specdata.loc[specdata['id'] == output1]
                #print(query2)
                #print(query1["mes_id_name"].item())
                if query2["name"].item() != 'None':
                    #print(query1["mes_id_name"])
                    #if i == 0:
                        #output3 += output2 + " :"
                    output3 = output3 + " " + query2["name"].item()
                i += 1
            if output3 != "None":
                return(str(output3))