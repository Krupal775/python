# what is try and except function in oops?


while(True):
    print("press q to quit..!")
    a = input("enter a num: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print("you enter a number is greater than 6")
    except Exception as e:
        print(e)

print('thanks for playing game..!') 