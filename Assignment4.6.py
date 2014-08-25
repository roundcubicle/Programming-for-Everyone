'''def computepay(h,r):
    if hrs > 40: 
        ot = hrs - 40
        ot_rate = rate * 1.5
        ot_pay = ot_rate * ot
        full_pay = pay + ot_pay
	else:
        print hrs *rate
    return full_pay'''

def computepay(h,r):
    if hrs > 40:
        pay = 40 * rate
        ot = hrs -40
        ot_rate = rate * 1.5
        full_pay = ot_rate *ot + pay
    else:
        full_pay = hrs * rate
    return full_pay



hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Pay Rate:"))
#pay = hrs * rate    
print hrs,rate
p = computepay(5,3)
print p
