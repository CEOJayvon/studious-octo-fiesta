def paintJobEstimator(sqft,cph,ppg):
    cost_of_paint = (sqft/110)*ppg
    cost_of_work = (sqft/110)*8*cph
    return round(cost_of_paint + cost_of_work,2)
sqft = 200
cph = 15
ppg = 25

#print(paintJobEstimator(sqft,cph,ppg)
    
