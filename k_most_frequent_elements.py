#!/usr/bin/env python
import sys
import heapq

def K_most_frequent_elements():
    lines=sys.stdin.readlines()
    
    size=int(lines[0].strip(" \r\n"))
    k=int(lines[-1].strip(" \r\n"))
    dic1={}
    for i in range(size):
        index=i+1
        element=lines[index].strip(" \r\n")
        if element in dic1:
            dic1[element]=dic1[element]+1
        else:
            dic1[element]=1
            
    list1=[(value, key) for key, value in dic1.iteritems()]
    
    if k<=len(list1):
        list2=heapq.nlargest(k,list1)
    else:
        list2=heapq.nlargest(size,list1)
        
    for new_element in list2:
        sys.stdout.write("%s\n" %(new_element[1])) #newelement=(value,key)
   
    
if __name__=="__main__":
    K_most_frequent_elements()
