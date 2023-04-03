#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:18:42 2023

@author: charan
"""

class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self,data):
        
        newnode = Node(data)
        print(newnode.data)
        if self.head == None:
            
            self.head = newnode
            self.tail = self.head
            self.length+=1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.length+=1
        
    def prepend(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
            self.length+=1
        else:
            newnode.next = self.head
            self.head = newnode
            self.length+=1
            
    def printlist(self):
        if self.head == None:
            print("linked list is empty")
        else:
            curr = self.head
            while curr!= None:
                
                print(curr.data,end = ' ')
                curr = curr.next 
            print()
            
    def insert(self,data,index):
        newnode = Node(data)
        if index >= self.length:
            if index > self.length:
                print("cannot insert at that position")
            self.tail.next = newnode
            self.tail = newnode
            self.length+=1
        elif index == 0:
            newnode.next = self.head
            self.head = newnode
            self.length+=1
        else:
            curr = self.head
            for i in range(index-1):
               curr = curr.next
            newnode.next = curr.next
            curr.next =  newnode
        self.length+=1

    def delete_by_value(self,value):
        if self.head == None:
            print("there nothing to delete")
        curr = self.head
        if self.head.data == value:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
                self.length-=1
            return
        while(curr.next != None and curr.next != value):
            curr = curr.next
        
        if curr.next != None:
            curr.next = curr.next.next
            if curr.next == None:
                self.tail = curr
            self.length-=1
            return
        else:
            print("given value doest exist in the list")
            
    
    def delete_by_position(self,index):
        if self.head == None:
            print("list is empty")
        if index == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length-=1
            return
        if index >= self.length:
            if index > self.length:
                print("cannot remove from that position as it is greater than the size")
            position = self.length-1
            curr = self.head
            for i in range(position - 1):
                curr = curr.next 
            curr.next = curr.next.next 
            
            if curr.next.next == None:
                self.tail = curr
            return 
        
if __name__ == '__main__':

    my_linked_list = LinkedList()
    my_linked_list.printlist()
#Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.printlist()
    
    my_linked_list.prepend(4)
    my_linked_list.printlist()
    
    my_linked_list.insert(2,4)
    my_linked_list.printlist()
            
            
            
            
