'''
Created on Mar 18, 2022

@author: wreid
'''
import pandas as pd 

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
    
    def sysdataquery(self):
        
        systemdata = pd.read_csv("Data/GameAssets/Serial/Data/Message/system_en.txt", delimiter='\t', names=['id', 'value'])
        
        sq = systemdata.query('id == @self.value')
    
        #print (sq)
    
        if sq.empty == False:
            sdout = sq['value'].item()
            return(sdout)
                 
        pass
        #print(r)
        '''
        Constructor
        '''
        