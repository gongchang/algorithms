#!/usr/bin/env python
class PriorityQueue:
    """use a min-heap to implement the Priority Queue,
    and the heap is represented as an array
    """
    def __init__(self,array1=[]):
        self.minheap=array1
    
    #because python is 0-based, so instead of having 2k and 2k+1
    #for the children, we now have 2k+1 and 2k+2
    #where k is the position of the parent
    def parent(self,position):
        return (position-1)/2
    
    def left_child(self,position):
        return 2*position+1
    
    def right_child(self,position):
        return 2*position+2
    
    def heapify(self,parent):
        """used to maintain the heap properties
        """
        left=self.left_child(parent)
        right=self.right_child(parent)
        min_pos=parent
        length_of_heap=len(self.minheap)
        
        #compare to see whether the parent node's value is the smaller
        #than its children,
        #if not,the min_pos will be used to hold the position of its smallest children
        
        if left<length_of_heap and self.minheap[left]<self.minheap[parent]:
            min_pos=left
        if right<length_of_heap and self.minheap[right]<self.minheap[min_pos]:
            min_pos=right
        
        #if the min_pos is not the parent,
        #swtiching between the parent and its smallest child is needed,
        #and recursion will be called
        if min_pos!=parent:
            self.minheap[parent],self.minheap[min_pos]=self.minheap[min_pos],self.minheap[parent]
            self.heapify(min_pos)
        
    def build_minheap(self):
        length_of_heap=len(self.minheap)
        for i in range(length_of_heap/2,-1,-1):
            self.heapify(i)
        return self.minheap
    
    def insert(self,item):
        """append the new item to the end of the minheap array;
        Then compare it with its parent.If the element is smaller, swap it
        with its parent.Until it is no longer smaller or the root is reached
        """
        self.minheap.append(item)
        curr_pos=len(self.minheap)-1
        count=0 #for time complexity count
        while self.minheap[curr_pos]<self.minheap[self.parent(curr_pos)] and curr_pos!=0:
            self.minheap[curr_pos],self.minheap[self.parent(curr_pos)]=self.minheap[self.parent(curr_pos)],self.minheap[curr_pos]
            curr_pos=self.parent(curr_pos)
    
    def remove(self):
        """remove the smallest item;
            put the last item at the root and then re-heapify the minheap;
            return the smallest item.
        """
        min_item=self.minheap[0]
        last_item=self.minheap.pop()
        #if the minheap is not empty
        if len(self.minheap)>0:
            self.minheap[0]=last_item
            self.heapify(0)
        return min_item
    
class PriorityQueueModified:
    """
    Time Complexity is included in the 
    use a min-heap to implement the Priority Queue,
    and the heap is represented as an array
    """
    def __init__(self,array1=[]):
        self.minheap=array1
    
    #because python is 0-based, so instead of having 2k and 2k+1
    #for the children, we now have 2k+1 and 2k+2
    #where k is the position of the parent
    def parent(self,position):
        return (position-1)/2
    
    def left_child(self,position):
        return 2*position+1
    
    def right_child(self,position):
        return 2*position+2
    
    def heapify(self,parent):
        """used to maintain the heap properties
        """
        left=self.left_child(parent)
        right=self.right_child(parent)
        min_pos=parent
        length_of_heap=len(self.minheap)
        
        count=0 #time complexity measure
        
        #compare to see whether the parent node's value is the smaller
        #than its children,
        #if not,the min_pos will be used to hold the position of its smallest children
        
        if left<length_of_heap and self.minheap[left]<self.minheap[parent]:
            min_pos=left
        if right<length_of_heap and self.minheap[right]<self.minheap[min_pos]:
            min_pos=right
        
        #if the min_pos is not the parent,
        #swtiching between the parent and its smallest child is needed,
        #and recursion will be called
        if min_pos!=parent:
            self.minheap[parent],self.minheap[min_pos]=self.minheap[min_pos],self.minheap[parent]
            self.heapify(min_pos)
            count=count+1
        return count
    
    def build_minheap(self):
        length_of_heap=len(self.minheap)
        count=0
        for i in range(length_of_heap/2,-1,-1):
            count=count+self.heapify(i)
        return self.minheap,count
    
    def insert(self,item):
        """append the new item to the end of the minheap array;
        Then compare it with its parent.If the element is smaller, swap it
        with its parent.Until it is no longer smaller or the root is reached
        """
        count=0  #for time complexity count
        self.minheap.append(item)
        count=count+1
        curr_pos=len(self.minheap)-1
        while self.minheap[curr_pos]<self.minheap[self.parent(curr_pos)] and curr_pos!=0:
            self.minheap[curr_pos],self.minheap[self.parent(curr_pos)]=self.minheap[self.parent(curr_pos)],self.minheap[curr_pos]
            curr_pos=self.parent(curr_pos)
            count=count+2
        return count
    
    def remove(self):
        """remove the smallest item;
            put the last item at the root and then re-heapify the minheap;
            return the smallest item.
        """
        count=0
        min_item=self.minheap[0]
        last_item=self.minheap.pop()
        #if the minheap is not empty
        count=count+1
        if len(self.minheap)>0:
            self.minheap[0]=last_item
            count=count+1
            count=count+self.heapify(0)
        return min_item,count      