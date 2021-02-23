try:
    a = int(input('enter a num= '))
    c = 1/a
    print(c)
except Exception as e:
    print(e)
    exit()

finally:
    print('we are done')