'''English = int(input("Enter English Marks = "))
Hindi = int(input("Enter Hindi Marks = "))
Maths = int(input("Enter Maths Marks = "))
Science = int(input("Enter Science Marks = "))
SST = int(input("Enter SST Marks = "))

Total= English+Hindi+Maths+Science+SST
print("SUM OF ALL SUBJECTS =",Total)
percentage = (Total/500)*100
print("PERCENTAGE IS = ", percentage)

if percentage>=32:
    print("PASSED")
else:
    print("Fail")'''

Student1=input("\n\nEnter your Name = ")

English = int(input("Enter English Marks = "))
Hindi = int(input("Enter Hindi Marks = "))
Maths = int(input("Enter Maths Marks = "))
Science = int(input("Enter Science Marks = "))
SST = int(input("Enter SST Marks = "))

print()

print(Student1,"Result")
Total= English+Hindi+Maths+Science+SST
print("SUM OF ALL SUBJECTS =",Total)
percentage = (Total/500)*100
print("PERCENTAGE IS = ", percentage)

if percentage>=60:
    print(f"{Student1} New iphone")
elif percentage<=60:
    print(f"{Student1} Baap se chudega")


print()


Student2=input("\n\nEnter your name = ")

English1 = int(input("Enter English Marks = "))
Hindi1 = int(input("Enter Hindi Marks = "))
Maths1 = int(input("Enter Maths Marks = "))
Science1 = int(input("Enter Science Marks = "))
SST1 = int(input("Enter SST Marks = "))

print()

print(Student2,"Result")
Total= English1+Hindi1+Maths1+Science1+SST1
print("SUM OF ALL SUBJECTS =",Total)
percentage1 = (Total/500)*100
print("PERCENTAGE IS = ", percentage1)

if percentage1>=60:
    print(f"{Student2} Shabash Ladle")
elif percentage1<=60:
    print(f"{Student2} Meri belt kaha hai")

print ()

print(Student1,"vs",Student2)


if percentage>=percentage1:
    print(f'''      
                へ   ♡      ╱|、
           ૮  -   ՛ )      (`   -  7
            /   ⁻  ៸|       |、⁻〵
        乀 (ˍ, ل ل        じしˍ,)ノ {Student1}  Moj kardi bete''')
elif percentage1>=percentage:
    print(f'''    
             へ   ♡      ╱|、
           ૮  -   ՛ )      (`   -  7
            /   ⁻  ៸|       |、⁻〵
        乀 (ˍ, ل ل        じしˍ,)ノ {Student2}  Moj kardi ladle''')



