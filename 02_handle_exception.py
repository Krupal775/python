try:
    a = int(input("enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print('Please enter a valid value')
except ZeroDivisionError as e:
    print('make sure you can not divided by value zero')

print("Thanks for using this code")