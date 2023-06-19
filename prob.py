prob_absent=float(input("Enter probability of absent :"))
prob_friday=float(input("Enter probability that is friday :"))
prob=(prob_absent/prob_friday)*100
print("Probability percentage absent on friday is :",int(prob),"%")