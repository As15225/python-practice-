# nice_weather=False
# print("go out for a walk" if nice_weather else "Watch a movie at home")

# Number=int(input("Enter a number"))
# print("is a Even number"if Number%2==0 else "Number is odd")



# Number=int(input("Enter First  Number = "))
# Number2=int(input("Enter Second Number =  "))
# c="number 1 is bigger than 2"
# d="number 2 is bigger than 1"

# print(c if Number>Number2 else d)


# a=int(input("number 1 =  "))
# b=int(input("number 2 =  "))
# c=a
# a=b
# b=c
# print(a,b)


#series divisible by 7 
# a=7
# for i in range(1,11):
#     print("7 x ",i,"=" ,a*i)
    

#income slab
salary=int(input("Enter Your Salary = "))
if salary<=500000:
    print("0% TAX")
elif salary<=750000:
    print("10% TAX = ",(salary*10)/100)
elif salary<=100000:
    print("20% TAX0: = ",(salary*20)/100)
else :
    print("30% TAX =",(salary*30)/100)

