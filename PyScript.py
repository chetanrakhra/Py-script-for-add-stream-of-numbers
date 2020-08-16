sum = 0

while True:
    UserInput = input("Enter the item price or press q to quit: \n")
    if UserInput != 'q':
        sum = sum + int(UserInput)
        print(f"Your total so far.. {sum}")

    else:
        print(f"Thank your bill is: {sum}. Thank you for shopping with us")
        break
