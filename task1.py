import random

ourList = list()
num = 5
count = 0
while (count < 11):
    ourList.append(random.randint(1,10)) # generates ten random numbers
    count += 1

# we assign belowFive numbers in ourList below 5   
belowFive = [i for i in ourList if i < num]

#print numbers below five
print (belowFive)