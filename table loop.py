# a=int(input("Enter the Digit = "))
# for i in range (1,11):
#     print(f"{a} x {i} = {a*i}")


# money=int(input("Enter the amount of money for per month = "))
# goal=int(input("enter the GOAL"))

# for i in range(1,13):
#     total_saved = money*12
# print(f"Total amount of money saved in 12th months {total_saved}")
# if total_saved>=goal:
#     print("Goal reached! You can buy the setup.")
# elif total_saved<=goal:
#     print ("not enough money ")
# else: 
#     print("Not enough yet, keep saving!")



weekly_petrol=int(input("Enter your weekly petrol budget = "))
total_spent=0
for i in range(1,7):
    daily_cost= int(input("Enter petrol cost for today = "))
    total_spent= total_spent+daily_cost
print(f"Total spent : rupees is {total_spent}")

if weekly_petrol>=total_spent:
    print("Great job! You stayed within your budget")
elif weekly_petrol<=total_spent:
    print("Alert! You exceeded your budget")






