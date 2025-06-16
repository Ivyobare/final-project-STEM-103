from sparkle_sips import *
print("WELCOME TO SPARKLE AND SIPS")
#Get customer information
user_name = input("Enter your first name: ")

#Get the age
legal_age()

#Input of more info
num_ofpeople()

#Getting the order and order info
list = menu_drinks(user_name)

#Getting order total
order_total,order = 0, []

#Taking drink order
order_total = place_order(list, order_total, order)

#Tip inclusion
tip = int(input("Would you like to include a tip on the order? If yes enter amout: "))
total_withtip = order_total + tip




#print receipt
yes = True
input("Would you like a printed receipt?")
if True :
    print("Here is your receipt. Thankyou.")

else :
    print("Receipt sent through phone. Thankyou .")    

#Fun saying
print("Good vibes , Good drink, Godd times.Have a good one!!")