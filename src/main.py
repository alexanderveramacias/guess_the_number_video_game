from random import randint

minimum_number=1

maximum_number=20

number_of_attemps=0

user_name=input("enter your username: ")


random_number=randint(minimum_number,maximum_number)

#print(random_number)

print(f"welcome {user_name} you have to guess a number from {minimum_number} to {maximum_number}")

while number_of_attemps < 7:
    print("guess the number :)")
    user_number=int(input())

    number_of_attemps += 1

    if random_number==user_number:
        #print(f"you did {number_of_attemps} tries")
        break
    
    elif random_number < user_number:
        print("the number is less")
    elif random_number > user_number:
        print("the number is greater")
if random_number==user_number:
        print(f"you did {number_of_attemps} tries")
if random_number != user_number:
    print("you lost")     



