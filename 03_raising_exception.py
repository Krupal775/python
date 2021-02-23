def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('This is a value error...!!')

a = int(increment(input('enter num= ')))
print(a)