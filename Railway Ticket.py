# 1.The person is booking the railway ticket based on their age and the number of tickets they want to purchase.The 
# prices are regular price : rs.50, senior citizen (Age 60 and above) price : rs.30 and for the children 
# age 12 and below price is :rs.20.Find out total cost based on the their age and the number of tickets and display it.


# sample input : 

# enter your age : 65
# enter no of tickets : 3


# sample output :

# Total cost for 3 tickets : 90



age = int(input("Enter your age: "))
num_tickets = int(input("Enter number of tickets: "))

# Initialize ticket prices
regular_price = 50
senior_citizen_price = 30
children_price = 20

# Determine the price based on age
if age >= 60:
    ticket_price = senior_citizen_price
elif age <= 12:
    ticket_price = children_price
else:
    ticket_price = regular_price

# Calculate total cost
total_cost = ticket_price * num_tickets

# Display the total cost
print(f"Total cost for {num_tickets} tickets: {total_cost}")