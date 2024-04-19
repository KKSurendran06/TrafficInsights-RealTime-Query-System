import math

L1=40
L2=20
L3=25
L4=15

sum=L1+L2+L3+L4
greenlight= False
   
def no_of_vehicles(L1,L2,L3,L4):
    Lane=[L1,L2,L3,L4]
    for num in Lane:
        ratio = (num/sum) * calTime(sum)
        checklight(ratio)

def calTime(sum):
    if sum<=25:
        T=60
        return T
    elif sum<=50:
        T=120
        return T 
    elif sum<=75:
        T=180
        return T
    elif sum<=100:
        T=240
        return T 
    elif sum<=125:
        T=300
        return T 
    else:
        T=360 
        return T         

def checklight(duration):
    greenlight=True
    print("GREEN")
    i=0
    while i < math.floor(duration):
        if i<0:
            print("RED")
            return
        i=i-1

no_of_vehicles(L1,L2,L3,L4)