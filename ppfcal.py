print ("Enter your yearsly inverstment ...")
inverstment = int(raw_input())
print ("Enter current interest rate ...")
current_interest_rate = float(raw_input())

def ppfcal(inverstment,current_interest_rate):
  if inverstment > 0 and current_interest_rate > 0 :
    deposite = 0
    for i in range(1,16):
      interestrate = (deposite+inverstment)*current_interest_rate / 100
      deposite = deposite + inverstment + interestrate
      #print ("After %d year your deposite amount is %d" % (i,deposite))
    print ("After 15 years you will get %d" % deposite  )
  else:
    print ("Please don\'t provide interestrate or inverstment 0 or less then 0.")

ppfcal(inverstment,current_interest_rate)
