def score(x, y):
    distance = (x**2 + y**2) ** 0.5 #calc distance from 0,0

    if distance > 10:
        return 0 #outside target
    
    elif distance > 5:
        return 1 #outer circle

    elif distance > 1:
        return 5 #middle circle

    else: 
        return 10 #inner circle
