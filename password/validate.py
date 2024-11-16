text = input("Password: ")

check_upper = 0
check_digit = 0

for i in range(0, len(text)):       
    if(text[i].isupper() == True):
        check_upper = 1
        break 
 
for i in range(0, len(text)):
    if(text[i] >= "0" and text[i] <= "9"):
        check_digit = 1
        break

if(len(text) < 8):
    print("Smaller than 8 characters")
elif(check_digit == 0 and check_upper == 0):
    print("There are no numbers or upper case letters!")
elif(check_digit == 0):
    print("There are no numbers!") 
elif(check_upper == 0):
    print("There are no upper case letters!")
else:
    print("This password is Strong!")    
