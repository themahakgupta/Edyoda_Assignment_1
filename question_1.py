#Write a python program to write fibonacci series between 0 to 50
range_start=int(input("Enter starting value of range="))
range_end=int(input("Enter endinmg value of range ="))
fib_1=0
fib_2=1
print("The fibonacci series in range between 0 to 50 is:")
for i in range(range_start,range_end):
    if i<=1:
        fib=i
    else:
        fib=fib_1+fib_2
        fib_1=fib_2
        fib_2=fib
    print(fib)



