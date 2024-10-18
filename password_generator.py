import random
lower_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters=[i.upper() for i in lower_letters]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
lower_len=int(input("Enter the no of lower case alphabets "))
upper_len=int(input("enter the  no.of upper case aplhabets"))
numbers_len=int(input("Enter the  no.of numbers "))
symbols_len=int(input("Enter the no.of symbols"))
password=""
for i in range(lower_len):
    password=password+random.choice(lower_letters)
for i in range(upper_len):
    password=password+random.choice(upper_letters)
for i in range(numbers_len):
    password=password+str(random.choice(numbers))
for i in range(symbols_len):
    password=password+random.choice(symbols)
password="".join(random.sample(password,len(password)))
print(password)