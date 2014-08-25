hrs = raw_input("Enter Hours:")
h = float(hrs)
base_pay = 10.50
'''ot = 10.50 * 1.5
ot_hrs = h -40
ot_pay = ((40*base_pay) + (ot*ot_hrs))'''

if h > 40:
    ot = 10.50 * 1.5
    ot_hrs = h -40
    ot_pay = 40 * base_pay + ot *ot_hrs
    print "Your total pay is: $" + str(ot_pay)
else:
    print "hi"
