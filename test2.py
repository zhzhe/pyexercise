
x= 0
y= 0
z= 0

for x in range(0,30):
    for y in range(0,10):
        for z in range(0,10):
            sum = 1600*x+4000*y+4600*z 
            #print(sum)
            if sum == 35000 :
                if x+y+z==11:
                    print(x,y,z+15)
