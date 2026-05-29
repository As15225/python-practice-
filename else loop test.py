Correct_pin=2727
Enter_pin=int(input("Enter Your PIN = "))
while Enter_pin!=Correct_pin:
       print("///WRONG PIN, ACCESS DENIED///")
       Enter_pin=int(input("Wrong Pin, Try again please = "))
       print("PIN Verified. Welcome User")
