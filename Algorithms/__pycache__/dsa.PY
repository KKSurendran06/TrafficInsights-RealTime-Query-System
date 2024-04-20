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

def findLaneTime(L1,L2,L3,L4):
    lane = [L1,L2,L3,L4]
    setNewLaneTime=[]
    for num in lane:
        ratio = (num/total_no_of_cars) * setTime
        setNewLaneTime.append(ratio)
    return setNewLaneTime

def dsa_function(data):
    global total_no_of_cars
    global setTime

    no_of_cars_in_lane1 = data[0]
    no_of_cars_in_lane2 = data[1]
    no_of_cars_in_lane3 = data[2]
    no_of_cars_in_lane4 = data[3]
    total_no_of_cars = no_of_cars_in_lane1+no_of_cars_in_lane2+no_of_cars_in_lane3+no_of_cars_in_lane4

    setTime = calTime(total_no_of_cars)
    newTime = findLaneTime(no_of_cars_in_lane1, no_of_cars_in_lane2, no_of_cars_in_lane3, no_of_cars_in_lane4)
    print(f'set traffic time to {setTime}')
    print(f'The new lane time will be {newTime}')