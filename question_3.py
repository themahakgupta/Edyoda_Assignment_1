# Write a python program to count the number of even and odd numbers from a given series
numbers=(1,2,3,4,5,6,7,8,9)
count_even=0
count_odd=0
for i in numbers:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Count of even numbers in above given series is=",count_even)
print("Count of odd numbers in above given series is=",count_odd)



