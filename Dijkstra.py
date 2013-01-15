#!/usr/bin/env python
#Not familiar enough with javascript to code up asap.js
#Here is an alternative I coded up with python

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
    
def Dijstra(graph,source): #V,vertices; E,edges; source,starting node
    """graph is a python dictionary
       V, a python list; graph.keys(); E, an adjacency list implementation of graph
    """
    trees=[] #used to store (distance,vertex_label) and later for building the min-heap,the reason why distance is put before vertex_label is because that is the item
    dic1={} #for storing the initializing distances,later is used to store the update distances
    for vertex in graph.keys():
        if vertex==source:
            trees.append((0,vertex))
            dic1[vertex]=0
        elif vertex in graph[vertex]: #if the vertex is directly connected to the source
            trees.append((1,vertex))
            dic1[vertex]=1
        else:
            trees.append((10000000,vertex))  #10000000 is used here as "infinity"
            dic1[vertex]=10000000
    heap1=PriorityQueue(trees)
    heap1.build_minheap()
    shortest_path=[]
    while len(heap1.minheap)!=0:  #when the heap is not empty
        u=heap1.remove() #get the vertex with the smallest distance
        shortest_path.append(u) #u=(distance,vertex_label)
        for node in graph[u[1]]: #for all the neighbors of node u
            distance=dic1[node]
            if u[0]+1<distance: #the relaxation condition
                dic1[node]=u[0]+1
                if heap1.minheap.count((distance,node))>0:
                    index1=heap1.minheap.index((distance,node))
                    heap1.minheap[index1]=(dic1[node],node)
                else:
                    pass
        heap1.heapify(0)
    return dic1  #return all the distances from source to the other nodes
if __name__=="__main__":
    #testing codes
    graph={'a':['b','c','d'],'b':['a','d','f'],'c':['a','d'],'d':['a','b','c','g'],'f':['b','g'],'g':['f','d']}
    source='b'
    dic2=Dijstra(graph,source)
    print dic2
    
    graph={1:[2,3,4],2:[4],3:[1],4:[1,2],}
    source=1
    dic3=Dijstra(graph,source)
    print dic3
    
 
