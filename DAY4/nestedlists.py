import copy
if __name__ == '__main__':
    
    l1=[]
    l2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append(name)
        l2.append(score)
        
    l=copy.deepcopy(l2)
    l=list(set(l))
    l.sort()
    val=l[1]
    r=[]
    
    for i in range(len(l2)):
        if l2[i]==val:
            r.append(l1[i])
    r.sort()
    for i in r:
        print(i)
        
    

    
        
    
