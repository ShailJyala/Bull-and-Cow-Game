import random


def guess_number():


    num = number()
   # print(num)
    attempts = 0      


    while True:
        try:
            guess = int(input("Guess a number between 100 and 999: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < num :
            cow_count = cow(guess,num)
            bull_count = bull(guess,num)
            dif = bull_count - cow_count
            print(f"{cow_count} Cow")
            print(f"{dif} Bull")
        elif guess > num:
            cow_count = cow(guess,num)
            bull_count = bull(guess,num)
            dif = bull_count - cow_count
            print(f"{cow_count} Cow")
            print(f"{dif} Bull")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            cow_count = cow(guess,num)
            bull_count = bull(guess,num)
            dif = bull_count - cow_count
            print(f"{cow_count} Cow")
            print(f"{dif} Bull")
            break
#Random Number Generator
       
def number():
    while True:
        num = random.sample(range(0, 10), 3)  
        if num[0] == 0:
            continue
        generated_number = int(''.join(map(str, num)))  
        return generated_number

#Number of Cows
def cow(guess, number):
    count = 0
    for i in range(3):
        if str(guess)[i] == str(number)[i]:
            count += 1
    return count        
   
#Number of Bulls
def bull(guess,number) :
    count = 0
    while True :
           
        for i in range(3):
            if str(guess)[0] == str (number)[i] :
                count += 1
       
        for i in range(3):
            if str(guess)[1] == str (number)[i] :
                count += 1
       
        for i in range(3):
            if str(guess)[2] == str (number)[i] :
                count += 1
        break
    return count
   

guess_number()