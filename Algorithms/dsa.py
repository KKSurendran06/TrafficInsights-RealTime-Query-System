import math

no_of_cars_lane1=40
no_of_cars_lane2=20
no_of_cars_lane3=25
no_of_cars_lane4=15

SUM = no_of_cars_lane1+no_of_cars_lane2+no_of_cars_lane3+no_of_cars_lane4

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

setTime = calTime(SUM)

def laneTime(L1,L2,L3,L4):
    lane = [L1,L2,L3,L4]
    setNewLaneTime=[]
    for num in lane:
        ratio = (num/SUM) * setTime
        setNewLaneTime.append(ratio)
    return setNewLaneTime    
   
def main():
    newTime = laneTime(no_of_cars_lane1, no_of_cars_lane2, no_of_cars_lane3, no_of_cars_lane4)
    print(f'set traffic time to {setTime}')
    print(f'The new lane time will be {newTime}')

main()