num = int(input('enter a num:'))

table = [(num*i) for i in range(1,11)]
print(table)

with open('1.txt','a+') as f:
    f.write(str(table))
    f.write('\n')