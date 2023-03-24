
dic = {1:[1] , 2:[1,1,1]}
stage = int(input("how many stages: "))
if stage >=2:
    for i in range(3,stage+1):
        dic[i]=[]
        for a in range(i+1):
            dic[i].append(a)
      
    for y in range(3,stage+1):
        for item in range(stage+1):
            if item == 0:
                dic[y][0] = 1
            else:
                try:
                    new_value = dic[y-1][item-1] + dic[y-1][item]
                    dic[y][item] = new_value
                except IndexError:
                    pass
                
            dic[y][-1] = 1
    
    
    for x in range(1,stage+1):
        print(dic[x])
        print()
