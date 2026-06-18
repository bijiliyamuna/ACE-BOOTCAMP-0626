if __name__ == '__main__':
    N = int(input())
    
list=[]
for i in range(N):
    cmd=input()
    ch_list=cmd.split( )
    if (ch_list[0]=="insert"):
        list.insert(int(ch_list[1]),int(ch_list[2]))
        
    if (ch_list[0]=="print"):
        print(list)
        
    if (ch_list[0]=="remove"):
        list.remove(int(ch_list[1]))
    
    if (ch_list[0]=="append"):
        list.append(int(ch_list[1]))
    
    if (ch_list[0]=="sort"):
        list.sort()
    
    if (ch_list[0]=="pop"):
        list.pop()
    
    if (ch_list[0]=="reverse"):
        list.reverse()
