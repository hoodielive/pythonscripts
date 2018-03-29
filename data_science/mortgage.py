principal = 5000000.00
rate = 0.05
payment = 2700.00
total_paid = 0.0

while principal > 0: 
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment 

print('Total Paid: ' + total_paid)
