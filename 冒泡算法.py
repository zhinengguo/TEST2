#coding=utf-8
'''
Created on 2016-3-29

@author: zouxuan
bug#2
'''

def stringSort(mylist):
    for i in range(len(mylist)):
        for i in range(len(mylist)-1):
            if mylist[i]>mylist[i+1]:
                mylist[i],mylist[i+1]=mylist[i+1],mylist[i]
                print mylist[i]
    print mylist
    
if __name__=='__main__':
    stringSort(mylist=['a',4,23,4,2,7,'c','b',3,9])

