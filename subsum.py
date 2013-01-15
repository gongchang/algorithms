#!/usr/bin/env python
import sys

def subsum(filename1,output_name1):
    file1=open(filename1,'r')
    lines=file1.readlines()
    
    file2=open(output_name1,'w')
    length=len(lines)
    total=int(lines[0].strip("\r\n"))
    index=1
    for count in range(total):
        record=lines[index].strip("\r\n").split(" ")
        n=int(record[0])
        new_record=[int(k) for k in record[1:]]
        newrecord=sorted(new_record)
        sum_record=sum(newrecord)
        t=[[0]*(sum_record+1)]*(n+1)
        c=[[set("")]*(sum_record+1)]*(n+1)
        t[0][0]=1
        for j in range(1,sum_record+1):
            for i in range(1,n+1):
                if (j>=newrecord[i]):
                    for k in range(i):
                        if t[k,j-newrecord[i]]==1:
                            t[i,j]=1
                            c[i,j]=c[k,j-newrecord[i]].add(i)
                        else:
                            pass
                else:
                    pass
            if sum(t[:,j])>=2:
                for row in range(n+1):
                    file2.write("Case #%s:\n" %(count+1))
                    count_row=0
                    if t[row,j]==1 and count_row<2:
                        count_row+=1
                        line=[str(newrecord[seq]) for seq in c[row,j]]
                        newline="".join(line)
                        file2.write("%s\n" %(newline))
                break
            file2.write("Case #%s: %s\n" %(count+1,"Impossible"))
        index=index+1
    
if __name__=="__main__":
    subsum(sys.argv[1],sys.argv[2])
