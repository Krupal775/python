# <----find n factorial--->

num = int(input("Enter the num: "))
result = 1
for i in range(num,0,-1):
    result = result*i

print("factorial of",num,"is",result)