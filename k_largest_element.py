#!/usr/bin/env python
import sys
import heapq
def k_largest_element():
    """use heap sort
      k=4 here in this code
    """
 
    lines=sys.stdin.readlines()
    
    size=int(lines[0].strip(" \r\n"))
    list1=[]
    for i in range(size):
        index=i+1
        element=int(lines[index].strip(" \r\n"))
        list1.append(element)
        
    list2=heapq.nlargest(4,list1)
    for new_element in list2:
        sys.stdout.write("%s\n" %(new_element))
   
    
if __name__=="__main__":
    k_largest_element()
