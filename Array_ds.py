#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:14:38 2023

@author: charan
"""

class MyArray():
    
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def push(self,data):
        self.length+=1
        self.data[self.length-1] = data
    
    def get(self,index):
        return self.data[index]
    
    def pop(self):
        last_item = self.data[self.length -1]
        del self.data[self.length - 1]
        self.length -=1
        return last_item
    
    def delete(self,index):
        for i in range(index , self.length-1 ):
            self.data[i ] = self.data[i+1]
            
        del self.data[self.length -1]
        self.length-=1
        
    def insert(self,data,index):
        self.length+=1
        for i in range(self.length-1, index , -1 ):
            self.data[i] = self.data[i -1]
            
        self.data[index] = data
        
        
        

var1  = MyArray()
var1.push(5)
var1.push(4)

print(var1.get(0))
