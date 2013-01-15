#!/usr/bin/env python
from optparse import OptionParser
#I use python2.6 and thus use optparse for command line flag


def sawmill():
    """usage example:sawmill.py -L 10 -v 1,2,5,7,9
      -L: length
      -v: positions for sawing
      
    A dynamic programming solution
    
    Time Complexity: O(k^3), there are O(k^2) sub-problems,
        and each takes O(k) to compute. Therefore, O(k^3) time in total
    """
    parser = OptionParser()
    parser.add_option("-L", "--length", dest="length")
    parser.add_option("-v", "--output", dest="position_string")
    (options, args) = parser.parse_args()
    
    metal_length=int(options.length)
    position_string=options.position_string
    position_list=[int(i) for i in position_string.split(",")]
    #print position_string[2]
    position_length=len(position_list)
    #cut array contain valuess for the cut postions at each cut,cut[i]
    cut=[0]
    cut.extend(position_list)
    cut.append(metal_length)
    #print cut
    #cost matrix, cost[i,j] 
    cost=[]
    #pointers are used to store the traceback markers for printing out the path
    pointers=[]
    for i in range(position_length+2):
        cost.append(['X']*(position_length+2))
        pointers.append(['X']*(position_length+2))
    #print cost
    for i in range(0,position_length+2):
        cost[i][i]=0
    for f in range(1,position_length+2):
        for i in range(1,position_length+2-f):
            j=i+f
            
            list_value=[]
            list_pointer=[]
            for k in range(i,j):
                list_value.append(cost[i][k]+cost[k+1][j])
                list_pointer.append(k)
            minimum=min(list_value)
            #print minimum
            cost[i][j]=cut[j]-cut[i-1]+minimum
            pointers[i][j]=list_pointer[list_value.index(minimum)]
            
    #print pointers
    #print cost[1][position_length+1]
    optimal_cost=cost[1][position_length+1]
    
    queue=[]
    queue.append([1,position_length+1])
    set1=[]
    set1.append([1,position_length+1])
    
    #obtain the path(cutting order)
    path=[]
    while len(queue)!=0:
        #print queue
        i=queue[0][0]
        j=queue[0][1]
        #print i,j
        queue.pop(0)
        k=pointers[i][j]
        #print k
        if k!='X':
            #print cut[k],"\t"
            path.append(cut[k])
            if [i,k] not in set1:
                queue.append([i,k])
                set1.append([i,k])
            if [k+1,j] not in set1:
                queue.append([k+1,j])
                set1.append([k+1,j])
        else:
            pass
    dic1={}
    dic1["sawmill_result"]=[{"minimum_cost":optimal_cost},{"cutting_order":path}]
    print dic1["sawmill_result"]
                        

    
if __name__=="__main__":
    sawmill()