number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)
