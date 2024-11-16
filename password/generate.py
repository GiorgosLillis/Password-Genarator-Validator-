import random

lenght = random.randint(8,20)
data = []

for i in range(0, lenght):
    set = random.randint(1,3)

    if(set == 1):
      data.append(random.randint(1,9))    
    elif(set == 2):
      upper_let = random.randint(65,90)
      data.append(chr(upper_let))
    elif(set == 3):
      lower_let = random.randint(97,122)
      data.append(chr(lower_let)) 

password = str(data)
password = password.replace(",", "").replace(" ", "").replace("'", "")
print("Password:" +password)
  

