def evencheck(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def divisiblecheck(num, check):
    if num % check == 0:
        print("Divisilbe evenly")
    else:
        print("Not Divisible")


num = int(input("Enter a Number"))

evencheck(num)

check = int(input("Enter a Number to Divide"))
divisiblecheck(num, check)
