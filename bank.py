from os import name
#!Bank account amount
#?Subtact iteam from Bank account

name = ["Catza", "ninjafiveo", "GrumTheEGirl"]

accounts = {
    name[0]: 5000.25,
    name[1]: 5000.25,
    name[2]: 5000.25
}

accounts[name[1]]

bob = input("Welcome, What's your name?")

if bob == name[0]:
    print("Hello Catza! you're starting balance is $" + str(accounts[name[0]]))
elif bob == name[1]:
    print("Hello ninjafiveo! you're starting balance is $" + str(accounts[name[1]]))
elif bob == name[2]:
    print("Hello GrumTheEGirl! you're starting balance is $" + str(accounts[name[2]]))

frank = input("How much do you want to deposit?")
dyno = input("Looks like you went shopping. What did you buy?")
iteamprice = float(input("How much was the iteam?"))

timmy = accounts[bob] - iteamprice

print("Your current bank amount is now $" + str(timmy))