#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:33:27 2023

@author: charan
"""

class HashTable():
    def __init__(self,size):
        
        self.length = size
        
        self.data = [None]*size
        

    def _hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.length
        return hash 
    
            
    def set(self,key,value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key,value]]
        else:
            self.data[hash] = [key,value]
        
        print(self.data)
            
    def get(self,key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                 if self.data[hash][i][0] == key:
                     
                     return self.data[hash][i][1]
        return None
    
    
    
    def keys(self):
        keys_array = []
        for i in range(self.length):
            if self.data[i]:
                if len(self.data[i]>1):
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0])
        return keys_array
                    
                    
    def values(self):
        values_array = []
        for i in range(self.length):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
                    
        return values_array
    
    
    

new_hash = HashTable(2)
print("here",new_hash)
#{'size': 2, 'data': [None, None]}

new_hash.set('one',1)
new_hash.set('two',2)

print("here2",new_hash)

print(new_hash.get('one'))
    
    
    
            
